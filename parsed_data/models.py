from django.db import models

# Create your models here.

class SnsData(models.Model):
    author = models.TextField()
    text = models.TextField()
    hashtag = models.TextField()
    link = models.URLField()

    
