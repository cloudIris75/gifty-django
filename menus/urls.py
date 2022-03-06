from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('brands/', views.BrandListView.as_view(), name='brand-list'),
    path('menus/', views.menu_list, name='menu-list'),
    path('menus/<int:id>/', views.menu_brand, name='menu-brand'),
    path('menus/<int:id>/<str:ct>/', views.menu_category, name='menu-category'),
    path('calculator/', views.calculator, name='calculator')
]
