# tracker/urls.py
# tracker/urls.py

# tracker/urls.py

from django.urls import path
from .views import home, shopping_list_view, create_shopping_list, edit_shopping_list, delete_shopping_list, favicon, add_expense

urlpatterns = [
    path('', home, name='home'),
    path('shopping-list/', shopping_list_view, name='shopping_list'),
    path('create-shopping-list/', create_shopping_list, name='create_shopping_list'),
    path('edit-shopping-list/<int:pk>/', edit_shopping_list, name='edit_shopping_list'),
    path('delete-shopping-list/<int:pk>/', delete_shopping_list, name='delete_shopping_list'),
    path('favicon.ico', favicon, name='favicon'),
    path('add-expense/<int:shopping_list_id>/', add_expense, name='add_expense'),  # Add this line for the new view
]


