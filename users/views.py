from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from users.forms import NewSignupForm
from django.shortcuts import render
from django.urls import reverse
from auth_helper import get_sign_in_flow, get_token_from_code, store_user, remove_user_and_token, get_token
from graph_helper import *


# Create your views here.
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


def initialize_context(request):
    context = {}
    error = request.session.pop('flash_error', None)
    if error != None:
        context['errors'] = []
    context['errors'].append(error)
    # Check for user in the session
    context['user'] = request.session.get('user', {'is_authenticated': False}
                                          )
    return context


def sign_in(request):
    # Get the sign-in flow
    flow = get_sign_in_flow()
    # Save the expected flow so we can use it in the callback
    try:
        request.session['auth_flow'] = flow
    except Exception as e:
        print(e)
    # Redirect to the Azure sign-in page
    return HttpResponseRedirect(flow['auth_uri'])


def sign_out(request):
    # Clear out the user and token
    remove_user_and_token(request)
    return HttpResponseRedirect(reverse('signin'))


def callback(request):
    # Make the token request
    result = get_token_from_code(request)
    # Get the user's profile from graph_helper.py script
    user = get_user(result['access_token'])
    # Store user from auth_helper.py script
    store_user(request, user)
    return HttpResponseRedirect(reverse('signin'))
