from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile


# Create your models here.
class Post(models.Model):
    image = models.FileField(upload_to='media/')
    description = models.TextField(max_length=300, null=True, blank=True)
    created_data = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(Profile, related_name='likes', null=True, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.description

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=400)
    commenter = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
