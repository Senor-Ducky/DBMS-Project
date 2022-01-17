from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
             'type':'text',
             'name':'username',
             'placeholder':'Username', 
             'class':'box',
             'required':''
        })

        self.fields['email'].widget.attrs.update({
             'type':'email',
             'name':'email',
             'placeholder':'Email', 
             'class':'box',
             'required':''
        })

        self.fields['password1'].widget.attrs.update({
             'type':'password',
             'name':'password1',
             'placeholder':'Password', 
             'class':'box',
             'required':''
        })

        self.fields['password2'].widget.attrs.update({
             'type':'password',
             'name':'password2',
             'placeholder':'Confirm Password', 
             'class':'box',
             'required':''
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']