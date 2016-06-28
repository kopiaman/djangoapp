from django.contrib import admin

# Register your models here.
from .models import Post,Review,Like

admin.site.register(Post)
admin.site.register(Review)
admin.site.register(Like)

