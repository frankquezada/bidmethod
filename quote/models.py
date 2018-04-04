from django.contrib.auth.models import User
from django.db import models

class UserFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    archived = models.DateTimeField(null=True)
    file = models.FileField(upload_to="uploads")

    def __str__(self):
        return self.title