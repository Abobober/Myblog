from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length = 300)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)

    def __str__ (self) -> str:
        return self.title
