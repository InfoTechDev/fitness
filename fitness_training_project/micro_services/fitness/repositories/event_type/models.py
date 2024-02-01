import uuid

from django.db import models


class EventType(models.Model):
    id = models.UUIDField(max_length=50, editable=False, primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
