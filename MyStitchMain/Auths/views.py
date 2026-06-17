from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, AppUserForm, LoginForm
from django.shortcuts import redirect, render

def signup_view(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        appuser_form = AppUserForm(request.POST)

        if signup_form.is_valid() and appuser_form.is_valid():
            user = signup_form.save()
            appuser = appuser_form.save(commit=False)
            appuser.user = user
            appuser.save()
            login(request, user)
            return redirect('home')
    else:
        signup_form = SignupForm()
        appuser_form = AppUserForm()

    return render(request, 'Auths/signup_page.html', {
        'signup_form': signup_form,
        'appuser_form': appuser_form
    })

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # note: request as first arg
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'Auths/login_page.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)