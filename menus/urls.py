from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brands/', views.BrandListView.as_view(), name='brand-list'),
    path('menus/', views.MenuListView.as_view(), name='menu-list'),
    path('menus/<int:id>/', views.menu_brand, name='menu-brand'),
    # path('menus/<int:id, str:category>/' views.menu_category, name='menu_category'),
    path('calculator/', views.calculator, name='calculator')
]
