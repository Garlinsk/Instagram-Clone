from django import forms
from .models import Image, Comment, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

    def __init__(self, *args, **kwargs):
        super(NewCommentForm, self).__init__(*args, **kwargs)
        # self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['comment'].label = False
        self.helper.show_label_comment = False


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 2, 'cols': 10, }),
        }


# class RegisterForm(RegistrationForm):
#     first_name = forms.CharField(max_length=255)
#     last_name = forms.CharField(max_length=255)

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name',
#                   'email', 'password1', 'password2',)

#     def __init__(self, *args, **kwargs):
#         super(RegistrationForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         for fieldname in ['username', 'password1', 'password2']:
#             self.fields[fieldname].help_text = None
#         self.helper.form_show_labels = True
        
