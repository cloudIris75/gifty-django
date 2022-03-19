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

        gifticon_ct = request.POST.get('gifticon-ct', '')
        gifticon_name = request.POST.get('gifticon-name', '')
        gifticon_count = request.POST.get('gifticon-count', 1)

        menu1_ct = request.POST.get('menu1-ct', '')
        menu1_name = request.POST.get('menu1-name', '')
        menu1_count = request.POST.get('menu1-count', 1)
        
        # gifticons = Q()
        # if id and id != '0':
        #     gifticons &= Q(brand_id = id)
        #     gifticon_list = Gifticon.objects.filter(gifticons)
        #     if ct and ct != '':
        #         gifticons &= Q(category = ct)
        #         gifticon_list = Gifticon.objects.filter(gifticons)
        # else:
        #     gifticon_list = Gifticon.objects.all()

        def item_price(model, name, count):
            if name:
                global item
                item = model.objects.get(name=name)
                if count:
                    global price
                    price = int(item.price) * int(count)
            else:
                item = False
                price = 0
            return item, price

        item_price(Gifticon, gifticon_name, gifticon_count)
        gifticon_item = item
        gifticon_price = price

        item_price(Menu, menu1_name, menu1_count)
        menu1_item = item
        menu1_price = price

        result = menu1_price

        data = {
            'brands': brands,
            'id': int(id),

            'gifticon_ct': gifticon_ct,
            'gifticon_name': gifticon_name,
            'gifticon_count': int(gifticon_count),
            # 'gifticon_list': gifticon_list,
            'gifticon_item': gifticon_item,
            'gifticon_price': gifticon_price,

            'menu1_ct': menu1_ct,
            'menu1_name': menu1_name,
            'menu1_count': int(menu1_count),
            'menu1_item': menu1_item,
            'menu1_price': menu1_price,

            'result': result
        }

        return render(request, 'menus/calculator.html', data)
