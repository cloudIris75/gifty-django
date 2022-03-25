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

        menu2_ct = request.POST.get('menu2-ct', '')
        menu2_name = request.POST.get('menu2-name', '')
        menu2_count = request.POST.get('menu2-count', 1)

        menu3_ct = request.POST.get('menu3-ct', '')
        menu3_name = request.POST.get('menu3-name', '')
        menu3_count = request.POST.get('menu3-count', 1)

        menu4_ct = request.POST.get('menu4-ct', '')
        menu4_name = request.POST.get('menu4-name', '')
        menu4_count = request.POST.get('menu4-count', 1)

        menu5_ct = request.POST.get('menu5-ct', '')
        menu5_name = request.POST.get('menu5-name', '')
        menu5_count = request.POST.get('menu5-count', 1)

        def item_list(model, id, ct):
            global name_list
            name = Q()
            if id and id != '0':
                name &= Q(brand_id = id)
                name_list = model.objects.filter(name)
                if ct and ct != '':
                    name &= Q(category = ct)
                    name_list = model.objects.filter(name)
            else:
                name_list = model.objects.all()
            return name_list

        def item_price(model, name, count):
            global item
            global price
            if name:
                item = model.objects.get(name=name)
                if count:
                    price = int(item.price) * int(count)
            else:
                item = False
                price = 0
            return item, price

        item_list(Gifticon, id, gifticon_ct)
        gifticon_list = name_list
        item_price(Gifticon, gifticon_name, gifticon_count)
        gifticon_item = item
        gifticon_price = price

        item_list(Menu, id, menu1_ct)
        menu1_list = name_list
        item_price(Menu, menu1_name, menu1_count)
        menu1_item = item
        menu1_price = price

        item_list(Menu, id, menu2_ct)
        menu2_list = name_list
        item_price(Menu, menu2_name, menu2_count)
        menu2_item = item
        menu2_price = price

        item_list(Menu, id, menu3_ct)
        menu3_list = name_list
        item_price(Menu, menu3_name, menu3_count)
        menu3_item = item
        menu3_price = price

        item_list(Menu, id, menu4_ct)
        menu4_list = name_list
        item_price(Menu, menu4_name, menu4_count)
        menu4_item = item
        menu4_price = price

        item_list(Menu, id, menu5_ct)
        menu5_list = name_list
        item_price(Menu, menu5_name, menu5_count)
        menu5_item = item
        menu5_price = price

        result = menu1_price + menu2_price + menu3_price + menu4_price + menu5_price

        data = {
            'brands': brands,
            'id': int(id),

            'gifticon_ct': gifticon_ct,
            'gifticon_name': gifticon_name,
            'gifticon_count': int(gifticon_count),
            'gifticon_list': gifticon_list,
            'gifticon_item': gifticon_item,
            'gifticon_price': gifticon_price,

            'menu1_ct': menu1_ct,
            'menu1_name': menu1_name,
            'menu1_count': int(menu1_count),
            'menu1_list': menu1_list,
            'menu1_item': menu1_item,
            'menu1_price': menu1_price,

            'menu2_ct': menu2_ct,
            'menu2_name': menu2_name,
            'menu2_count': int(menu2_count),
            'menu2_list': menu2_list,
            'menu2_item': menu2_item,
            'menu2_price': menu2_price,

            'menu3_ct': menu3_ct,
            'menu3_name': menu3_name,
            'menu3_count': int(menu3_count),
            'menu3_list': menu3_list,
            'menu3_item': menu3_item,
            'menu3_price': menu3_price,

            'menu4_ct': menu4_ct,
            'menu4_name': menu4_name,
            'menu4_count': int(menu4_count),
            'menu4_list': menu4_list,
            'menu4_item': menu4_item,
            'menu4_price': menu4_price,

            'menu5_ct': menu5_ct,
            'menu5_name': menu5_name,
            'menu5_count': int(menu5_count),
            'menu5_list': menu5_list,
            'menu5_item': menu5_item,
            'menu5_price': menu5_price,

            'result': result
        }

        return render(request, 'menus/calculator.html', data)
