from django.db import models

# Create your models here.
class Customer(models.Model):
  fname = models.CharField(max_length=100)
  lname = models.CharField(max_length=100)
  phone = models.CharField(max_length=15)
  email = models.EmailField(unique=True)
  address = models.TextField(blank=True,null=True)

class Order(models.Model):
  customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders'
    )
  quantity_ordered = models.IntegerField()
  order_date = models.DateTimeField(auto_now_add=True)
  total_amount = models.DecimalField(max_digits=10, decimal_places=2)