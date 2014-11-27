from django.db import models

# Create your models here.

class tokens(models.Model):
    token = models.CharField(max_length=40)
    user_id = models.IntegerField()