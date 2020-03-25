from django import forms
from django.contrib.auth.models import User
from simple_app.models import UserProfileInfo


class UserInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('department', 'profile_pic')
