from django.contrib import admin
from .models import BlogPost
from django.contrib.auth.models import Group, User

# Register your models here.
admin.site.register(BlogPost)

#Unregsiter
admin.site.unregister(Group)
admin.site.unregister(User)
# admin.site.unregister(BlogPost)

admin.site.site_header = 'Blogging Admin Panel'
admin.site.site_title = 'Admin Panel'
admin.site.index_title = 'Site admin'

