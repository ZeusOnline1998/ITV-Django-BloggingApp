from django.contrib import admin
from .models import BlogPost
from django.contrib.auth.models import Group, User
from django.utils.html import format_html

class BlogPostAdmin(admin.ModelAdmin):

    list_display = ('title', 'content_colored', 'create_date') #Display the fields in the admin panel
    list_filter = ('create_date', 'publish_date') #Add filter options
    search_fields = ('content',) #Create a search bar based on the field provided if more field provided then it will provide only one search with multiple field search
    list_per_page = 5 #Pagination
    date_hierarchy = 'create_date' #Create a heirarchical structure to filter data
    list_display_links = ('content_colored',) #Provides the link to edit the data implicitly
    list_editable = ('title',) #Can edit the field in the base panel

    def content_colored(self, obj):  #Format the html of the given column
        return format_html(f'<span style="color: red">{obj.content}</span>')

    


    


# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)

#Unregsiter
admin.site.unregister(Group)
admin.site.unregister(User)
# admin.site.unregister(BlogPost)

admin.site.site_header = 'Blogging Admin Panel'
admin.site.site_title = 'Admin Panel'
admin.site.index_title = 'Site admin'

