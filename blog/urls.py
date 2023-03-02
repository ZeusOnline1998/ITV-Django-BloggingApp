from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name='home'),
    path('post_detail/<int:id>/', views.post_detail_view, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/edit/<int:id>', views.edit_post, name='edit_post'),
    path('post/delete/<int:id>', views.delete_post, name='delete_post'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
]