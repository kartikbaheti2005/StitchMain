from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.

genderChoice = [
    ("Male","Male"),
    ("Female","Female"),
]

class AppUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(unique = True)
    address = models.TextField(max_length=500)
    Gender = models.CharField(max_length = 20, choices=genderChoice, default="Male")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username