# blog/admin.py

from django.contrib import admin
from .models import Post
from .forms import PostForm

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    prepopulated_fields = {'slug': ('title',)}  # Asegúrate de que este campo coincida con el campo en el modelo
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')

admin.site.register(Post, PostAdmin)
