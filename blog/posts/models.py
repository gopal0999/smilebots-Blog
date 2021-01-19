from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class PostLike(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # many user many likes
    likes = models.ManyToManyField(User,related_name='post_user',blank=True , through=PostLike)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # to return list of data in descending order of the id
        # to get the latest posts
        ordering = ['-id']