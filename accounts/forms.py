from django import forms
from django.contrib.auth.models import User



class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=50, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your username'})
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'your password'})
    )



class UserRegisterForm(forms.Form):
    username = forms.CharField(
        max_length=50, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your username'})
    )
    email = forms.CharField(
        max_length=50, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your email'})
    )
    password_1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'your password'})
    )
    password_2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'your password'})
    )


    def clean_email(self):
        email = self.cleaned_data['email'] # first is_valid active, after this method
        user = User.objects.filter(email=email) # use get == error!
        if user.exists(): # this method for check exists (django )
            # you can use from "django.core.exceptions import ValidationError" but not different
            raise forms.ValidationError('this is email already exist.') # for show that, you should to turn off HTML validation

        return email

    
    def clean_password_2(self):
        password_1 = self.cleaned_data['password_1']
        password_2 = self.cleaned_data['password_2']
        if password_1 != password_2:
            raise forms.ValidationError('Password must be the same.')
        
        return password_2