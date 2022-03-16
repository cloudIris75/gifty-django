from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from django.db.models import Q
from menus.models import Brand, Gifticon, Menu

class IndexTemplateView(TemplateView):
    template_name = 'menus/index.html'

class BrandListView(ListView):
    model = Brand
    ordering = ['id']

class MenuView(View):
    def get(self, request, id=None, ct=None):
        context = dict()
        context['id'] = id
        context['ct'] = ct

        brands = Brand.objects.all()
        context['brands'] = brands

        menus = Q()
        if id:
            menus &= Q(brand_id = id)
            menu_list = Menu.objects.filter(menus)
            if ct:
                menus &= Q(category = ct)
                menu_list = Menu.objects.filter(menus)
        else:
            menu_list = Menu.objects.all()

        # ordering = order
        # menu_list = Menu.objects.filter(menus).order_by(ordering)
        
        context['menu_list'] = menu_list

        return render(request, 'menus/menu_list.html', context=context)

def calculator(request):
    context = dict()

    brands = Brand.objects.all()
    context['brands'] = brands

    return render(request, 'menus/calculator.html', context=context)
