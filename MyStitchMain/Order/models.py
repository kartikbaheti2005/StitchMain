from django.db import models
from django.utils import timezone
from datetime import timedelta
from Auths.models import AppUser
from cloths.models import LowerBody, UpperBody

orderstatus = [
    ("New", "New"),
    ("Waiting", "Waiting"),
    ("Urgent", "Urgent"),
    ("Done", "Done"),
]

class Order(models.Model):
    customer = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    upperBody = models.ForeignKey(UpperBody, on_delete=models.CASCADE, null=True, blank=True)
    lowerBody = models.ForeignKey(LowerBody, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=orderstatus, default="New")
    in_time = models.DateTimeField(auto_now_add=True)
    days = models.PositiveIntegerField(default=7, help_text="Days to complete the order")
    out_time = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # On first save in_time isn't set yet, so compute after super() if needed
        if not self.pk:
            # New order — save first to get in_time, then compute out_time
            super().save(*args, **kwargs)
            self.out_time = self.in_time + timedelta(days=self.days)
            Order.objects.filter(pk=self.pk).update(out_time=self.out_time)
            self.auto_flag_urgent()
            return
        else:
            # Existing order — recompute out_time from in_time + days
            self.out_time = self.in_time + timedelta(days=self.days)
            self.auto_flag_urgent()
            super().save(*args, **kwargs)

    def auto_flag_urgent(self):
        """Set status to Urgent if out_time is within 2 days and not already Done."""
        if self.out_time and self.status != "Done":
            delta = self.out_time - timezone.now()
            if delta.total_seconds() <= 2 * 24 * 3600:
                self.status = "Urgent"

    def __str__(self):
        return f"Order #{self.pk} — {self.customer}"