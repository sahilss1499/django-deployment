from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    # widget for password field so that the field's input is not the same as a normal CharField
    password = forms.CharField(widget=forms.PasswordInput())
    #meta class is used for taking the fields(requierd) here in the forms.py to be presented to the user
    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
