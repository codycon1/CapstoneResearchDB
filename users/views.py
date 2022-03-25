from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from users.forms import NewSignupForm

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
