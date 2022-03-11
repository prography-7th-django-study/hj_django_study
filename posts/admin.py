from django.contrib import admin

from posts.models import Post, Comment, Member

admin.site.register([Post, Comment, Member])