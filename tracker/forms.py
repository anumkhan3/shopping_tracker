# tracker/forms.py

from django import forms
from .models import ShoppingList, Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'description', 'image']
