from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    account_type = models.CharField(max_length=10)