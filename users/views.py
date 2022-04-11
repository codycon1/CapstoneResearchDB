import json

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from auth_helper import get_sign_in_flow, get_token, store_user, remove_user_and_token, get_token_from_code
from graph_helper import *
from capstone import settings

# Create your views here.
""""
def user_signup(request):
    if request.method == 'POST':
        form = NewSignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = NewSignupForm()
    return render(request, 'registration/signup.html', {'form': form})
"""


def initialize_context(request):
    context = {}
    error = request.session.pop('flash_error', None)
    if error is not None:
        context['errors'] = []
        context['errors'].append(error)
    # Check for user in the session
    context['user'] = request.session.get('user', {'is_authenticated': False})
    return context


def sign_in(request):
    # Get the sign-in flow
    flow = get_sign_in_flow()
    try:
        request.session['auth_flow'] = flow
    except Exception as e:
        print(e)
    return HttpResponseRedirect(flow['auth_uri'])


def sign_out(request):
    remove_user_and_token(request)
    return HttpResponseRedirect(reverse('home'))

# 5f0a4be8-970a-47c2-b074-e3945d20e88f
# 2c58e05f-8a92-44fc-90e6-1ef89fb96ad3-- Staff
def checkStaff(x):
    for i in x['value']:
        if i == '2c58e05f-8a92-44fc-90e6-1ef89fb96ad3':
            return True
    return False


def callback(request):
    # Make the token request
    result = get_token_from_code(request)
    user = get_user(result['access_token'])
    isStaff = checkStaff(get_groups(result['access_token']))
    store_user(request, user, isStaff)
    return HttpResponseRedirect(reverse('home'))
