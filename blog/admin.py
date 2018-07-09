from django.contrib import admin
from .models import Post

admin.site.register(Post) # to ensure the post model created is visible on our, we need register it as shown (line 4)