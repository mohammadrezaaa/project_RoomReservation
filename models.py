from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_TA = models.BooleanField(default=False)
    is_Professor = models.BooleanField(default=False)
    is_Administrative = models.BooleanField(default=False)


class TA(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Administrative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
