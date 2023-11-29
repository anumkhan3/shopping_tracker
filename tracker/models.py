from django.db import models

# Create your models here.
# tracker/models.py



class ShoppingList(models.Model):
    name = models.CharField(max_length=100)



class Expense(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
