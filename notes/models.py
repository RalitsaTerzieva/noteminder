from django.db import models
from accounts.models import UserProfile


class Note(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='media/')
    date = models.DateTimeField()

    def __str__(self):
        return self.title


