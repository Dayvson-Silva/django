from django.db import models

# Create your models here.
class Biutarefas(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True , null=True)
    date = models.DateTimeField(auto_now_add=True)
    conclude = models.BooleanField(default=False)
