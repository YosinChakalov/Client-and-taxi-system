from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    Choises = (
        ('admin', 'Admin'),
        ('taxi', 'TAXI'),
        ('user', 'USER'),
    )
    role = models.CharField(max_length=20, choices=Choises, default='user')

    def __str__(self):
        return self.username

