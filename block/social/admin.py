from django.contrib import admin

from .models import Avatar, Post,Profile
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Avatar)