from django.db import models

# Create your models here.


class tasks(models.Model):
    id = models.SmallAutoField(primary_key=True, null=False, unique=True)
    title = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title