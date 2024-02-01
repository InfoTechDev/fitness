import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(max_length=50, editable=False, primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=150, unique=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
