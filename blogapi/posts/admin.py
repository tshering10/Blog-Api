from django.contrib import admin
from posts.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    search_fields = ['title', 'author__username']  # make posts searchable
    list_filter = ['author', 'created_at']         # add filters in sidebar
    ordering = ['-created_at']
admin.site.register(Post, PostAdmin)