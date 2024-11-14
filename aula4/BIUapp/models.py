from django.db import models

# Create your models here.
class Biuapp(models.Model):
    name= models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField(blank=True , null=True)
    stock = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
