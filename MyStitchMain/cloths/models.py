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

upperBodyChoice = [
    (" "," "),
    ("Shirt","Shirt"),
    ("Kurta","Kurta"),
    ("Kurti","Kurti"),
    ("Shrewani","Shrewani"),
    ("Coat","Coat"),
    ("Jacket","Jacket"),
    ("Blouse","Blouse"),
    ("Gown","Gown"),
    ("Frock","Frock"),
]
class Options(models.Model):
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.text
    

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
class UpperBody(models.Model):
    length = models.IntegerField(blank = True)
    shoulder = models.IntegerField(blank = True)
    armLength = models.IntegerField(blank = True)
    fourarmLength = models.IntegerField(blank = True)
    neck = models.IntegerField(blank = True)
    chest = models.IntegerField(blank = True)
    waist = models.IntegerField(blank = True)
    hips = models.IntegerField(blank = True)
    clothType = models.CharField(max_length=20, choices=upperBodyChoice, default="None")
    pocket = models.BooleanField(default=False)
    requirments = models.ForeignKey(Options, on_delete=models.CASCADE)


    def __str__(self):
        return self.clothType
