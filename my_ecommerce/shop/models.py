from django.db import models

# Create your models here.
# Represents a customer who can place multiple orders.
class Customer(models.Model):
  fname = models.CharField(max_length=100)#The first name of the customer
  lname = models.CharField(max_length=100)#The last name of gthe customer
  phone = models.CharField(max_length=15)#Phone number of the customer
  email = models.EmailField(unique=True)#The unique email address of the customer
  address = models.TextField(blank=True,null=True)#optional address of the customer

# Represents the orders placed by the customer
class Order(models.Model):
  customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders'
    )# Foreign key to the customer model. Defines a one to many relationship(a customer can place multiple orders)
  quantity_ordered = models.IntegerField()
  order_date = models.DateTimeField(auto_now_add=True)# automatically set date and time of when the order is placed
  total_amount = models.DecimalField(max_digits=10, decimal_places=2)# Total monetary value of the order