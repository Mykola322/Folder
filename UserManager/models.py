from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MySuperUser(AbstractUser):
    phone_number = models.CharField(max_length=16, default=None, null=True, blank=True)
    address = models.CharField(max_length=200, default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"