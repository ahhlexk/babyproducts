from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)