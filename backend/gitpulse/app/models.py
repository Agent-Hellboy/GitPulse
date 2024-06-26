# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Repository(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    repo_url = models.URLField()

    def __str__(self):
        return self.repo_url
