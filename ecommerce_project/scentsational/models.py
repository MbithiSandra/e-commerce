from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    #customer establishes a one-to-many relationship using ForeignKey
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders') #Deletes orders if the associated customer is deleted.
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2) #records the total cost of the order.

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"