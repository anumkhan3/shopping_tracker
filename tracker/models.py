# tracker/models.py

from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ShoppingList(BaseModel):
    name = models.CharField(max_length=100)

    def calculate_total_cost(self):
        total_cost = sum(expense.amount for expense in self.expense_set.all())
        return total_cost

class Expense(BaseModel):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='expense_images/', blank=True, null=True)  # Added image field

class ExpenseImage(models.Model):
    expense = models.ForeignKey('Expense', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='expense_images/')

