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
    def get(self, request):
        context = dict()

        brands = Brand.objects.all()
        context['brands'] = brands

        menu_list = Menu.objects.all()
        context['menu_list'] = menu_list

        return render(request, 'menus/menu_list.html', context=context)

    def post(self, request):
        brands = Brand.objects.all()

        id = request.POST.get('id', False)
        ct = request.POST.get('ct', False)
        od = request.POST.get('od', False)

        menus = Q()
        if id and id != '0':
            menus &= Q(brand_id = id)
            menu_list = Menu.objects.filter(menus)
            if ct and ct != 'category':
                menus &= Q(category = ct)
                menu_list = Menu.objects.filter(menus)
        else:
            menu_list = Menu.objects.all()

        if od:  
            if od == '이름순':
                ordering = 'name'
            elif od == '가격낮은순':
                ordering = 'price'
            elif od == '가격높은순':
                ordering = '-price'
        else:
            od = '이름순'
            ordering = 'name'
        
        menu_order = menu_list.order_by(ordering)

        data = {
            'brands': brands,
            'id': int(id),
            'ct': ct,
            'od': od,
            'menu_list': menu_order
        }

        return render(request, 'menus/menu_list.html', data)

def calculator(request):
    context = dict()

    brands = Brand.objects.all()
    context['brands'] = brands

    return render(request, 'menus/calculator.html', context=context)
