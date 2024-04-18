from django.contrib import admin
from .models import Comment, Wishlist, favourite, read

# Register your models here.

admin.site.register(Comment)
admin.site.register(Wishlist)
admin.site.register(favourite)
admin.site.register(read)
