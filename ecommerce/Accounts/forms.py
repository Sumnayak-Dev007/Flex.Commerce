from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from store.models import ProfileUser

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateUser(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("username","email")
        widgets = {
                'username': forms.TextInput(attrs={
                    'class': 'mt-1 ml-2 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                    'placeholder': 'Enter your username',
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
                    'placeholder': 'Enter your email',
                }),
        }

    def __init__(self, *args, **kwargs):
        super(UpdateUser, self).__init__(*args, **kwargs)
        
        for fieldname in ['username', 'email']:
                self.fields[fieldname].help_text = None

class UpdateProfile(forms.ModelForm):
    
    class Meta:
        model = ProfileUser
        fields = ("image",)
    widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'mx-auto mt-1 block w-full text-sm text-gray-500 rounded-md border border-gray-300 cursor-pointer focus:outline-none focus:ring-blue-500 focus:border-blue-500',
            }),
        }
