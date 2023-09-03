from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    body = models.CharField(max_length=100)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')

    def __str__(self):
        return f"{self.sender}: {self.receiver}"
