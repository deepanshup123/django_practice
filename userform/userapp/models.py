from django.db import models

# Create your models here.
class userForm(models.Model):
    username = models.CharField(max_length = 110)
    email = models.CharField(max_length = 110)
    phonenumber = models.CharField(max_length = 15)