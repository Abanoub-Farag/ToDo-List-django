from django.db import models

# Create your models here.


class Task(models.Model):
    id = models.SmallAutoField(primary_key=True, null=False, unique=True)
    title = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.title