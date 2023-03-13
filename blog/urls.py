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
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    #Passwor
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset-done/', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),    
]