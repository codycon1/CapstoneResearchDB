from django.contrib import admin
from django.urls import path

from users import views

urlpatterns = [
    path('signup', views.user_signup),
    path('signin', views.sign_in, name='signin'),
    path('signout', views.sign_out, name='signout'),
    path('callback', views.callback, name='callback'),
]
