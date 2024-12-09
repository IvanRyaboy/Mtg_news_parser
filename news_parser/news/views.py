from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import *
from .tasks import send_spam_email


menu = [{'title': 'Главная', 'url_name': 'index'},
        ]


def index(request):
    context = {
        'menu': menu,
    }
    return render(request, 'news/index.html', context=context)


def subscribe(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        contact_form = ContactForm(request.POST)

        if user_form.is_valid() and contact_form.is_valid():
            user = user_form.save()
            contact = contact_form.save()
            contact.user = user
            contact.save()
            send_spam_email.delay(user_form.cleaned_data.get('email'))

            context = {
                'user_form': user_form,
                'contact_form': contact_form,
                'menu': menu,
            }

            return redirect('index')

    else:
        user_form = UserForm()
        contact_form = ContactForm()

    context = {
        'user_form': user_form,
        'contact_form': contact_form,
        'menu': menu,
    }

    return render(request, 'news/subscribe.html', context=context)


def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    else:
        form = LoginUserForm()
    return render(request, 'news/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        change_subscription_form = ChangeSubscriptionForm(request.POST)

        if change_subscription_form.is_valid():
            contact = change_subscription_form.save(commit=False)
            contact.save()

            context = {
                'form': change_subscription_form,
                'user': user,
            }
    else:
        change_subscription_form = ChangeSubscriptionForm()
    context = {
        'form': change_subscription_form,
        'user': user,
    }
    return render(request, 'news/profile.html', context=context)
