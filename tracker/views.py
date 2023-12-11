from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .models import ShoppingList
from .forms import ExpenseForm

def home(request):
   if request.user.is_authenticated:
       return redirect('shopping_list')
   else:
       return redirect('login')
def favicon(request):
    return HttpResponse(status=204)

def shopping_list_view(request):
    shopping_lists = ShoppingList.objects.all()
    return render(request, 'tracker/shopping_list.html', {'shopping_lists': shopping_lists})

def create_shopping_list(request):
    if request.method == 'POST':
        name = request.POST['name']
        ShoppingList.objects.create(name=name)
        return redirect('shopping_list')
    return render(request, 'tracker/create_shopping_list.html')

def edit_shopping_list(request, pk):
    shopping_list = get_object_or_404(ShoppingList, pk=pk)

    if request.method == 'POST':
        shopping_list.name = request.POST['name']
        shopping_list.save()
        return redirect('shopping_list')

    return render(request, 'tracker/edit_shopping_list.html', {'shopping_list': shopping_list})

def delete_shopping_list(request, pk):
    shopping_list = get_object_or_404(ShoppingList, pk=pk)
    shopping_list.delete()
    return redirect('shopping_list')

def add_expense(request, shopping_list_id):
    shopping_list = get_object_or_404(ShoppingList, pk=shopping_list_id)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.shopping_list = shopping_list
            expense.save()
            return redirect('shopping_list')
    else:
        form = ExpenseForm()

    return render(request, 'tracker/add_expense.html', {'form': form, 'shopping_list': shopping_list})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('shopping_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

