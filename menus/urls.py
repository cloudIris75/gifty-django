from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brands/', views.BrandListView.as_view(), name='brand-list'),
    path('menus/', views.menu_list, name='menu-list'),
    path('menus/<int:id>/', views.menu_brand, name='menu-brand'),
    path('calculator/', views.calculator, name='calculator')
]
