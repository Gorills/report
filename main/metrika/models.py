from django.db import models


from home.models import Project
# Create your models here.


class Metrika(models.Model):
    token = models.CharField(max_length=500)
    counter = models.CharField(max_length=250)