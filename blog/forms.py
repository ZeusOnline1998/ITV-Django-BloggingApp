from django import forms
from .models import BlogPost

class PostBlogForm(forms.ModelForm):
    
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