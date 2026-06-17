from django.db import models
from Auths.models import AppUser
from cloths.models import LowerBody, UpperBody

# Create your models here.

orderstatus = [
    ("New","New"),
    ("Waiting","Waiting"),
    ("Urgent","Urgent"),
    ("Done","Done"),
]

class Order(models.Model):
    customer = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    upperBody = models.ForeignKey(UpperBody, on_delete=models.CASCADE, null=True, blank =True)
    lowerBody = models.ForeignKey(LowerBody, on_delete=models.CASCADE, null=True, blank =True)
    status = models.CharField(max_length=20, choices=orderstatus, default = "New")
    in_time = models.DateTimeField(auto_now=True)
    out_time = models.DateTimeField(auto_now=True)

