from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 300)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__ (self) -> str:
        return self.title
