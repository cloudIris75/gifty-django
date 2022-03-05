from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
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

def menu_brand(request, id):
    context = dict()
    menu_brand = Menu.objects.filter(brand_id=id)
    context['menu_list'] = menu_brand

    paginator = Paginator(menu_brand, 6)
    curr_page_num = request.GET.get('page')
    if curr_page_num is None:
        curr_page_num = 1
    page = paginator.page(curr_page_num)
    context['page_obj'] = page

    return render(request, 'menus/menu_list.html', context=context)

# def menu_category(request, id, category):
#     menu_category = Menu.objects.filter(brand_id=id, category=category)
#     return render(request, 'menus/menu_list.html', {'menu_category': menu_category})

def calculator(request):
    return render(request, 'menus/calculator.html')