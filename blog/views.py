from django.shortcuts import render, HttpResponse
from .models import BlogPost

# Create your views here.

def index(request):

    result = BlogPost.objects.all().order_by('-id')
    content = {
        'blogs' : result,
    }
    
    return render(request, 'blog/index.html', context=content)