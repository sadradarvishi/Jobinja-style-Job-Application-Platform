from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserEntity(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(null=False, max_length=20)
    last_name = models.CharField(null=False, max_length=20)
    username = models.CharField(null=False, unique=True, max_length=50)
    password = models.CharField(null=False, max_length=50)
    email = models.EmailField(null=False)
    phone_number = models.CharField(null=False, unique=True)
    experience = models.TextField()
    education = models.CharField(max_length=100, choices=[
        ('Associate degree', 'Associate degree'),
        ('Bachelors degree', 'Bachelors degree'),
        ('Masters degree', 'Masters degree'),
        ('Doctoral degree', 'Doctoral degree')
    ])
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
