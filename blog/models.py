from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    views = models.IntegerField(default=0)
    answers= models.IntegerField(default=0)
    likes= models.IntegerField(default=0)
    view_status= models.BooleanField(default=False)
    like_status=models.BooleanField(default=False)
    post_image=models.ImageField(upload_to='upload/images')

    def __str__(self):
        return str(self.id)

def generate_comment_id():
    last_comment_id=Comments.objects.all().order_by('cmnt_id').last().cmnt_id
    if last_comment_id:
        return last_comment_id + 1
    return 1001


class Comments(models.Model):
    cmnt_id=models.IntegerField(primary_key=True,default=generate_comment_id)
    comment =models.TextField(max_length=500)
    pid=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return str(self.cmnt_id)


# class Answer(models.Model):
#     pass
