from django.conf import settings
from django.db import models
from django.utils import timezone   
from django.urls import reverse
    
class Post(models.Model):
    title = models.CharField(max_length = 300)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse ('post_detail', args=[str(self.id)])
    

    def __str__ (self) -> str:
        return self.title
    