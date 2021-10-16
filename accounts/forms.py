from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=50, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your username'})
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'your password'})
    )
