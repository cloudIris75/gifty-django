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
        brands = Brand.objects.all().order_by('id')
        menu_list = Menu.objects.all().order_by('name')

        data = {
            'brands': brands,
            'menu_list': menu_list
        }

        return render(request, 'menus/menu_list.html', data)

    def post(self, request):
        brands = Brand.objects.all().order_by('id')

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

class Calculator(View):
    def get(self, request):
        brands = Brand.objects.all().order_by('id')

        data = {
            'brands': brands
        }

        return render(request, 'menus/calculator.html', data)

    def post(self, request):
        brands = Brand.objects.all().order_by('name')

        id = request.POST.get('id', 0)
        # ct = request.POST.get('ct', False)
        name = request.POST.get('name', '')
        gifticon_count = request.POST.get('gifticon-count', 1)
        
        gifticons = Q()
        if id and id != '0':
            gifticons &= Q(brand_id = id)
            gifticon_list = Gifticon.objects.filter(gifticons)
            # if ct and ct != 'category':
            #     gifticons &= Q(category = ct)
            #     gifticon_list = Gifticon.objects.filter(gifticons)
        else:
            gifticon_list = Gifticon.objects.all()

        if name:
            gifticon = Gifticon.objects.get(name=name)
            if gifticon_count:
                gifticon_price = int(gifticon.price) * int(gifticon_count)
        else:
            gifticon = False
            gifticon_price = 0

        data = {
            'brands': brands,
            'id': int(id),
            # 'ct': ct,
            'name': name,
            'gifticon_count': int(gifticon_count),
            'gifticon_list': gifticon_list,
            'gifticon': gifticon,
            'gifticon_price': int(gifticon_price),
        }

        return render(request, 'menus/calculator.html', data)
