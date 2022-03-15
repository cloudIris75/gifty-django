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

    menu_name = Menu.objects.order_by('brand_id', 'category', 'name')
    context['menu_name'] = menu_name
    menu_descending = Menu.objects.order_by('brand_id', 'category', 'price')
    context['menu_descending'] = menu_descending
    menu_ascending = Menu.objects.order_by('brand_id', 'category', '-price')
    context['menu_ascending'] = menu_ascending

    return render(request, 'menus/menu_list.html', context=context)    

def menu_brand(request, id):
    context = dict()
    context['id'] = id

    brands = Brand.objects.all()
    context['brands'] = brands

    menu_name = Menu.objects.filter(brand_id=id).order_by('category', 'name')
    context['menu_name'] = menu_name
    menu_descending = Menu.objects.filter(brand_id=id).order_by('category', 'price')
    context['menu_descending'] = menu_descending
    menu_ascending = Menu.objects.filter(brand_id=id).order_by('category', '-price')
    context['menu_ascending'] = menu_ascending

    return render(request, 'menus/menu_list.html', context=context)

def menu_category(request, id, ct):
    context = dict()
    context['id'] = id
    context['ct'] = ct

    brands = Brand.objects.all()
    context['brands'] = brands

    menu_name = Menu.objects.filter(brand_id=id, category=ct).order_by('name')
    context['menu_name'] = menu_name
    menu_descending = Menu.objects.filter(brand_id=id, category=ct).order_by('price')
    context['menu_descending'] = menu_descending
    menu_ascending = Menu.objects.filter(brand_id=id, category=ct).order_by('-price')
    context['menu_ascending'] = menu_ascending

    return render(request, 'menus/menu_list.html', context=context)

def calculator(request):
    context = dict()

    brands = Brand.objects.all()
    context['brands'] = brands

    # if request.GET.get('brand'):
    #     brand = request.GET.get('brand')
        
    #     if brand == '스타벅스':
    #         global id
    #         id = '1'
    #     elif brand == '투썸플레이스':
    #         id = '2'

    #     gifticon_brand = Gifticon.objects.filter(brand_id=id)
    # else:
    #     gifticon_brand = Gifticon.objects.all()
    
    # context['gifticon_list'] = gifticon_brand

    return render(request, 'menus/calculator.html', context=context)
