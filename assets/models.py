from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Asset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def average_price(self):
        purchases = self.purchase_set.all()
        total_qty = sum(p.quantity for p in purchases)
        if total_qty == 0:
            return 0
        total_cost = sum(p.price * p.quantity for p in purchases)
        return round(total_cost / total_qty, 2)
    
    def __str__(self):
        return self.name

class Purchase(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    quantity = models.FloatField()
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.asset.name}: {self.quantity} for {self.price}"