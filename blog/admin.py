from django.contrib import admin
from blog.models import Post,Comments

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','desc','author','views','likes','comments','like_status','view_status','post_image']

@admin.register(Comments)
class PostAdmin(admin.ModelAdmin):
    list_display=['cmnt_id','comment','pid']
