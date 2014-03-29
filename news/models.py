from django.db import models

# Create your models here.

class News(models.Model) :
    newstext = models.TextField()
    datetime = models.TimeField()