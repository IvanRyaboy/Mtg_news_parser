from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('subscribe/', subscribe, name='subscribe'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/<int:user_id>/', profile, name='profile'),
    ]
