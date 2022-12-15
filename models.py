from django.db import models
from .validators import file_size

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length= 100)
    datetime = models.DateTimeField(auto_now_add= True)
    videos = models.FileField(upload_to="youtube/%y")

    def __str__(self):
        return str(self.title)
