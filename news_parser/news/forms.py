from django import forms
from .models import *


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = 'username', 'email', 'password'
        widgets = {
            'password': forms.PasswordInput(),
        }


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('subscription',)


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ChangeSubscriptionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.get('instance', None)
        super(ChangeSubscriptionForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['subscription'].queryset = MagicNews.objects.filter(type=user.subscription)

    class Meta:
        model = Contact
        fields = ('subscription',)
