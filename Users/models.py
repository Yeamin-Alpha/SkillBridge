#models.py
from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/profile_images/', default='images/profile_images/default.jpg', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone=models.CharField(default="Enter number",max_length=11,null=True, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'
