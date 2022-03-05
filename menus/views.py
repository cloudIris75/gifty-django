from django.shortcuts import render
from django.views.generic import ListView
from menus.models import Brand, Gifticon, Menu

def index(request):
    return render(request, 'menus/index.html')

class BrandListView(ListView):
    model = Brand
    ordering = ['id']

class MenuListView(ListView):
    model = Menu
    ordering = ['id']
    paginate_by = 6

# def menu_brand(request, pk):
#     menu = Menu.objects.get(brand=pk)
#     return render(request, 'menus/menu_list.html', {'menu': menu})

def calculator(request):
    return render(request, 'menus/calculator.html')