from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post_detail/<int:id>/', views.post_detail_view, name='post_detail'),
    path('post/new/', views.post_new, name='post_new')
]