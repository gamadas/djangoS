from django import forms
from django.contrib.auth.models import User
from erma_app.models import UserProfileInfo

# for Validation
from django.core import validators

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():  # transparent I/O to/from DB behind
        model = User
        fields = ('username','email','password')


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('external_site','profile_image')




class MyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
