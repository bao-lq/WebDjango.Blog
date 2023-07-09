from django import forms
import re
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    email = forms.EmailField(label = 'Email')
    username = forms.CharField(label = 'Username', max_length = 30)
    password1 = forms.CharField(label= 'Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label= 'RE-enter Password', widget=forms.PasswordInput())

    # check password 
    def clean_password2(self):
        if ('password1') in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError('Invalid password')

    # check username 
    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'^\w+&', username):
            raise forms.ValidationError('Username has special characters')
        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username already exists')

    # create user 
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password2'])