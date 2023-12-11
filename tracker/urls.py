
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, shopping_list_view, create_shopping_list, edit_shopping_list, delete_shopping_list, favicon, add_expense, register


urlpatterns = [


path('register/', register, name='register'),

   path('shopping-list/', shopping_list_view, name='shopping_list'),
   path('create-shopping-list/', create_shopping_list, name='create_shopping_list'),
   path('edit-shopping-list/<int:pk>/', edit_shopping_list, name='edit_shopping_list'),
   path('delete-shopping-list/<int:pk>/', delete_shopping_list, name='delete_shopping_list'),
   path('favicon.ico', favicon, name='favicon'),
   path('add-expense/<int:shopping_list_id>/', add_expense, name='add_expense'),
]



if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)















