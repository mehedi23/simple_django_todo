from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Task(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="todo_list", null=True)
    tittle = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle