from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
from menus.models import Brand, Gifticon, Menu

class IndexTemplateView(TemplateView):
    template_name = 'menus/index.html'

class BrandListView(ListView):
    model = Brand
    ordering = ['id']

def menu_list(request):
    context = dict()

    brands = Brand.objects.all()
    context['brands'] = brands

    menu = Menu.objects.order_by('brand_id', 'category', 'name')
    context['menu_list'] = menu

    return render(request, 'menus/menu_list.html', context=context)    

def menu_brand(request, id):
    context = dict()
    context['id'] = id

    brands = Brand.objects.all()
    context['brands'] = brands

    menu_brand = Menu.objects.filter(brand_id=id).order_by('category', 'name')
    context['menu_list'] = menu_brand

    return render(request, 'menus/menu_list.html', context=context)

def menu_category(request, id, ct):
    context = dict()
    context['id'] = id
    context['ct'] = ct

    brands = Brand.objects.all()
    context['brands'] = brands

    menu_category = Menu.objects.filter(brand_id=id, category=ct).order_by('name')
    context['menu_list'] = menu_category

    return render(request, 'menus/menu_list.html', context=context)

def calculator(request):
    context = dict()

    brands = Brand.objects.all()
    context['brands'] = brands

    return render(request, 'menus/calculator.html', context=context)
