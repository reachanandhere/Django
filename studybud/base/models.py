from django.db import models
import uuid
# Create your models here.

class Room(models.Model):
    #host = 
    #topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants = models.
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return self.name