from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from menus.models import Brand, Gifticon, Menu

def index(request):
    return render(request, 'menus/index.html')

class BrandListView(ListView):
    model = Brand
    ordering = ['id']

def menu_list(request):
    context = dict()

    brands = Brand.objects.all()
    context['brands'] = brands

    menu = Menu.objects.order_by('brand_id', 'category')
    context['menu_list'] = menu

    paginator = Paginator(menu, 6)
    curr_page_num = request.GET.get('page')
    if curr_page_num is None:
        curr_page_num = 1
    page = paginator.page(curr_page_num)
    context['page_obj'] = page

    return render(request, 'menus/menu_list.html', context=context)    

def menu_brand(request, id):
    context = dict()
    context['id'] = id

    brands = Brand.objects.all()
    context['brands'] = brands

    menu_brand = Menu.objects.filter(brand_id=id)
    context['menu_list'] = menu_brand

    paginator = Paginator(menu_brand, 6)
    curr_page_num = request.GET.get('page')
    if curr_page_num is None:
        curr_page_num = 1
    page = paginator.page(curr_page_num)
    context['page_obj'] = page

    return render(request, 'menus/menu_list.html', context=context)

def menu_category(request, id, ct):
    context = dict()
    context['id'] = id
    context['ct'] = ct

    brands = Brand.objects.all()
    context['brands'] = brands

    menu_category = Menu.objects.filter(brand_id=id, category=ct)
    context['menu_list'] = menu_category

    paginator = Paginator(menu_category, 6)
    curr_page_num = request.GET.get('page')
    if curr_page_num is None:
        curr_page_num = 1
    page = paginator.page(curr_page_num)
    context['page_obj'] = page

    return render(request, 'menus/menu_list.html', context=context)

def calculator(request):
    return render(request, 'menus/calculator.html')