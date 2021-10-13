from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) # if user not found in DB, return None
            if user is not None:
                login(request, user) # this method => set user to request and use in MVT
                return redirect('blog:all_articles')

    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

