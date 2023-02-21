from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import BlogPost
from django.core.exceptions import ObjectDoesNotExist
from .forms import PostBlogForm
from django.utils import timezone

# Create your views here.

def index(request):

    result = BlogPost.objects.all().order_by('-id')
    content = {
        'blogs' : result,
    }
    
    return render(request, 'blog/index.html', context=content)

def post_detail_view(request, id):
    # try:
        
    #     data = BlogPost.objects.get(id=id)  ## get method to retrieve information 
    # except ObjectDoesNotExist:              ## preferably to use whenever server requests information through methods
    #     print("Object Not Found Error")

    data = get_object_or_404(BlogPost, id=id)   ## preferably use when end user request the information

    content = {
        'post' : data
    }
    return render(request, 'blog/post_detail.html', context=content)

def post_new(request):

    if request.method == 'POST':
        form_data = PostBlogForm(request.POST)

        if form_data.is_valid():
            post_data = form_data.save(commit=False)
            post_data.author = request.user
            post_data.create_date = timezone.now()
            post_data.publish_date = timezone.now()
            post_data.save()
            return redirect('home')
    else:
        form_data = PostBlogForm()
    return render(request, 'blog/post_new.html',{'form_data': form_data})