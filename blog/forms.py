from django import forms
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class PostBlogForm(forms.ModelForm):
    
    # title = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter blog title'}))
    class Meta:
        model = BlogPost
        fields = ('title', 'content')

        widget = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px',
                'placeholder': 'Enter blog title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'max-width: 400px',
            })
        }

class RegistrationForm(UserCreationForm):

    class Meta:           
        model = User      
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    email = forms.EmailField(
        max_length = 100,
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )

    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget = forms.TextInput(attrs={'class': 'form-control','' 'placeholder': 'Enter your first name'})
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'})
    )

    username = forms.CharField(
        max_length=100,
        required=True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'})
    )

    password1 = forms.CharField(
        min_length=8,
        required=True,
        widget = forms.PasswordInput(attrs= {'class': 'form-control', 'placeholder': 'Enter your password'})
    )

    password2 = forms.CharField(
        min_length=8,
        required=True,
        widget = forms.PasswordInput(attrs= {'class': 'form-control', 'placeholder': 'Confirm password'})
    )

    check = forms.BooleanField(
        required = True,
        widget = forms.CheckboxInput(attrs = {'class': 'form-check-input'})
    )


        
