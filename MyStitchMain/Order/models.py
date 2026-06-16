from django.db import models
from Auths.models import AppUser

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    