from django.db import models

lowerBodyChoice = [
    (" "," "),
    ("Pant","Pant"),
    ("Barmuda","Barmuda"),
    ("Paijama","Paijama"),
    ("Skirt","Skirt"),
    ("Leggings","Leggings"),
    ("Leggings","Leggings"),
]

# Create your models here.
class LowerBody(models.Model):
    length = models.IntegerField(blank = True)
    hips = models.IntegerField(blank = True)
    thies = models.IntegerField(blank = True)
    knee = models.IntegerField(blank = True)
    ankle = models.IntegerField(blank = True)
    ankle = models.IntegerField(blank = True)
    Clothtype = models.CharField(max_length = 20, choices = lowerBodyChoice, default ="None")
    #requirement = models.ForeignKey(Options, on_delete = models.CASCADE)

def __str__(self):
    return self.clothType
 

