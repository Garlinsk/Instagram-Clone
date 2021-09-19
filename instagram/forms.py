from django import forms
from .models import Image, Comment, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationForm


class RegisterForm(RegistrationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control names', 'placeholder': "First Name", 'label': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control names', 'placeholder': "Second Name", 'label': 'Second Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control names', 'placeholder': "Email Address", 'label': 'Email Address'}),
            'username': forms.TextInput(attrs={'class': 'form-control names', 'placeholder': "Username", 'label': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control ', 'type': 'password', 'placeholder': "Password", 'label': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Confirm Password", 'label': 'Confirm Password'}),
        }




class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['Author', 'image_name',
                   'pub_date', 'author_profile', 'likes']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 10, }),
        }


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['author', 'image', 'pub_date']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 1, 'cols': 10}),
       }

   

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 2, 'cols': 10, }),
        }


