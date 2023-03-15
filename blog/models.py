from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.html import format_html

# Create your models here.
class BlogPost(models.Model):

    def __str__(self):
        return self.title


    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)


    # def content_colored(self): #Format the html of the given column in models.py
    #     return format_html(f'<span style="color: red">{self.content}</span>')
