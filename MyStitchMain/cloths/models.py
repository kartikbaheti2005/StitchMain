from django.db import models

lowerBodyChoice = [
    (" "," "),
    ("Trouser","Trouser"),
    ("Barmuda","Barmuda"),
    ("Paijama","Paijama"),
    ("Skirt","Skirt"),
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

allClothsChoice = lowerBodyChoice + upperBodyChoice
allClothsChoice = [item for item in allClothsChoice if item != (" ", " ")]


buttonChoice = [
    ("Normal","Normal"),
    ("Snap","Snap"),
    ("Flat Shank","Flat Shank"),
    ("Hook","Hook"),
]

sleeveChoice = [
    ("Full","Full"),
    ("Half","Half"),
    ("No Sleeve","No Sleeve"),
]

trouserChoice = [
    ("Normal","Normal"),
    ("Pencil","Pencil"),
    ("",""),
]

# Create your models here.
class Options(models.Model):
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.text
    

class LowerBody(models.Model):
    length = models.IntegerField(default=0)
    hips = models.IntegerField(default=0)
    thigh = models.IntegerField(default=0)
    knee = models.IntegerField(default=0)
    ankle = models.IntegerField(default=0)
    pantBottom = models.IntegerField(default=0)
    uCrouch = models.IntegerField(default=0)
    clothType = models.CharField(max_length=20, choices=lowerBodyChoice, default=" ")
    requirements = models.ForeignKey(Options, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.clothType

class UpperBody(models.Model):
    length = models.IntegerField(default=0)
    chest = models.IntegerField(default=0)
    upperChest = models.IntegerField(default=0)
    waist = models.IntegerField(default=0)
    hips = models.IntegerField(default=0)
    shoulder = models.IntegerField(default=0)
    sleeves = models.IntegerField(default=0)
    biceps = models.IntegerField(default=0)
    armHold = models.IntegerField(default=0)
    elbow = models.IntegerField(default=0)
    collar = models.IntegerField(default=0)
    backLength = models.IntegerField(default=0)
    crossBack = models.IntegerField(default=0)
    bustLength = models.IntegerField(default=0)
    apexGap = models.IntegerField(default=0)
    bottomWidth = models.IntegerField(default=0)
    clothType = models.CharField(max_length=20, choices=upperBodyChoice, default=" ")
    pocket = models.BooleanField(default = False)
    button = models.CharField(max_length=20, choices=buttonChoice, default="Normal")
    sleeveType = models.CharField(max_length=20, choices=sleeveChoice, default="Full")
    requirments = models.ForeignKey(Options, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.clothType
    
class ClothPrice(models.Model):
    cloth_type = models.CharField(max_length=20, choices=allClothsChoice, default=" ", unique=True)
    base_price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.cloth_type} - ₹{self.base_price}"