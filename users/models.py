from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    subscriptions = models.ManyToManyField('User', related_name='subscribers')
    photo = models.ImageField(upload_to='profile-pictures/', null=True, blank=True)


class UserRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='from_users', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_users', on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)
