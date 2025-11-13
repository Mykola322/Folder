from django.db import models

# Create your models here.


class Planer(models.Model):
    user = models.ForeignKey("UserManager.MySuperUser", on_delete=models.CASCADE)
    contact = models.ForeignKey("PhoneBook.Contact", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(default=None, null=True, blank=True)
    meeting_date = models.DateTimeField()
    url = models.URLField(default=None, null=True, blank=True)
    place = models.CharField(default="Online")
    accept = models.BooleanField(default=None, null=True, blank=True)


class Meta:
        constraints = [
            models.UniqueConstraint(fields=['contact', 'date'], name='unique_contact_date'),
            models.UniqueConstraint(fields=['user', 'date'], name='unique_user_date')
        ]