from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    image = models.ImageField(upload_to='media/user_images')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'