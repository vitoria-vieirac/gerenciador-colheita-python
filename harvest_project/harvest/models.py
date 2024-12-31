from django.contrib.auth.models import User
from django.db import models

class Harvest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='harvests')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 
    location = models.CharField(max_length=255, default="Desconhecido")
    quantity_in_tons = models.CharField(max_length=255, default="Não informada", blank=True)
    seed_type = models.CharField(max_length=255)
    fertilizer = models.CharField(max_length=255, null=True, blank=True, default="Não informada")

    def __str__(self):
        return self.title
