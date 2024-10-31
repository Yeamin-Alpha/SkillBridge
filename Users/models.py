#models.py
from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/profile_images/', default='images/profile_images/default.jpg', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'
