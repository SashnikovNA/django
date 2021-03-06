from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name= 'возраст')
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
