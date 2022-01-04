from django.db import models

# Create your models here.

class userDetails(models.Model):

    username = models.CharField(max_length=50)
