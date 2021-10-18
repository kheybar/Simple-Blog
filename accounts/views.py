from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserLoginForm, UserRegisterForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect('blog:all_articles')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) # if user not found in DB, return None
            if user is not None:
                login(request, user) # this method => set user to request and use in MVT
                messages.success(request=request, message='you logged in successfully.', extra_tags='success') # befor redirect
                return redirect('blog:all_articles')
            else:
                messages.error(request=request, message='wrong username or password', extra_tags='warning') # extra_tags: for send anythings with message like bootstrap classes
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})



def user_register(request):
    if request.user.is_authenticated:
        return redirect('blog:all_articles')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password_1'])
            messages.success(request=request, message='you register successfully, now login.', extra_tags='success')
            return redirect('accounts:user_login')

    else:
        form = UserRegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})



def user_logout(request):
    logout(request)
    messages.success(request=request, message='you logout successfully', extra_tags='success')
    return redirect('blog:all_articles')