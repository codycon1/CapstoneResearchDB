from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('signup', views.user_signup, name='signup'),
    # path('login', views.sign_in, name="signin"),
    # path('logout', views.sign_out, name="signout"),
    # path('callback', views.callback, name="callback"),
]
