from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Profile(models.Model):
    image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(default=date.today(), null=True, blank=True)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username
