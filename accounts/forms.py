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
        label='confirm password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'your password'})
    )


    def clean_email(self):
        email = self.cleaned_data['email'] # first is_valid active, after this method
        user = User.objects.filter(email=email) # use get == error!
        if user.exists(): # this method for check exists (django )
            # you can use from "django.core.exceptions import ValidationError" but not different
            raise forms.ValidationError('this is email already exist.') # for show that, you should to turn off HTML validation

        return email

    
    # def clean_password_2(self):
    #     password_1 = self.cleaned_data['password_1']
    #     password_2 = self.cleaned_data['password_2']
    #     if password_1 != password_2:
    #         raise forms.ValidationError('Password must be the same.')
        
    #     return password_2
    
    
    # استفاده از این روش برای بررسی پسورد ها یا به عبارتی فیلدهایی که بهم مربوط هستند، درست نیست چرا که روش بهتری وجود داره
    # باید متود کلین رو آوررایدش کنیم
    def clean(self):
        cleaned_data = super().clean() # برای اینکه به کلین دیتا دست پیدا کنیم و کلین پیشفرض ران بشه، اول از سوپر استفاده میکنیم
        password_1 = cleaned_data.get('password_1') # با استفاده از گت میایم و مقدار رو میکشیم بیرون
        password_2 = cleaned_data.get('password_2')
        if password_1 and password_2:
            if password_1 != password_2:
                raise forms.ValidationError('Password must be the same.') # این ارور ها میره جز فرم ارور ها نه فیلد ارور ها

        # نیاز به ریترن چیزی نیست