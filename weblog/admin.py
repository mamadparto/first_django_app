from django.contrib import admin
from .models import Posts


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_create')
    ordering = ('datetime_create', 'status')


admin.site.register(Posts, PostsAdmin)
