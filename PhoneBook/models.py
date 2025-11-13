from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=16)
    email = models.EmailField(max_length=200, null=True, blank=True, default=None)
    address = models.CharField(max_length=200, null=True, blank=True, default=None)
    bio = models.TextField(null=True, blank=True, default=None)
    age = models.IntegerField(null=True, blank=True, default=None)
    profile_picture = models.ImageField(upload_to='.', null=True, blank=True, default=None)
    user = models.ForeignKey('UserManager.MySuperUser', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"