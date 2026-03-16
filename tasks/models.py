from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False, null=False, blank=False)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"