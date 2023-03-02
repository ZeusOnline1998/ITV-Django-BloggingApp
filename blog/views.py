from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import BlogPost
from django.core.exceptions import ObjectDoesNotExist
from .forms import PostBlogForm, RegistrationForm
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):

    result = BlogPost.objects.all().order_by('-id')
    content = {
        'blogs' : result,
    }
    
    return render(request, 'blog/index.html', context=content)

@login_required(login_url='login')
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
            messages.success(request, 'Data inserted successfully')
            return redirect('home')
    else:
        form_data = PostBlogForm()
        # messages.error(request, form_data.errors)
    return render(request, 'blog/post_new.html', context={'form_data': form_data})

def edit_post(request, id):
    post = get_object_or_404(BlogPost, id=id)    
    if request.method == 'POST':
        form_data = PostBlogForm(request.POST, instance=post)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Post Updated Successfully")
            return redirect('post_detail', id=id)
        else:
            pass
    else:
        form_data = PostBlogForm(instance=post)
    return render(request, 'blog/edit.html', {'form_data' : form_data})

def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    post.delete()
    messages.success(request, 'Your post has been deleted')
    return redirect('home')

def register(request):

    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was successfully created for {username}')
        else:
            messages.error(request, 'Error while creating account')
        return redirect('home')

    return render(request, 'register.html', {'form': form})