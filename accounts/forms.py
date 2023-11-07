from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password_1 = forms.CharField(max_length=50)
    password_2 = forms.CharField(max_length=50)
    phone = forms.PhoneNumberField()

    def clean_username(self):
        user = self.cleaned_data['username']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('این نام کاربری وجود دارد')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل از قبل وجود دارد')
        return email

    def clean_password_2(self):
        password1 = self.cleaned_data['password_1']
        password2 = self.cleaned_data['password_2']
        if password1 != password2:
            raise forms.ValidationError('گذرواژه مطابقت ندارد')
        elif len(password2) < 8:
            raise forms.ValidationError('گذرواژه خیلی کوتاه است')
        elif not any(x.isupper() for x in password1):
            raise forms.ValidationError(' گذرواژه باید حداقل یک حرف بزرگ داشته باشد')
        return password1
