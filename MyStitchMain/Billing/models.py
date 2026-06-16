from django.db import models
from cloths.models import ClothPrice
from Order.models import Order

# Create your models here.
class Bill(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    base_price = models.ForeignKey(ClothPrice, on_delete=models.DO_NOTHING)
    advance = models.DecimalField(max_digits=10, decimal_places=2)
    Remaning = models.DecimalField(max_digits=10, decimal_places=2)
    Discount = models.DecimalField(max_digits=10, decimal_places=2)
    Total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)