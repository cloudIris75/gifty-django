from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('brands/', views.BrandListView.as_view(), name='brand-list'),
    path('menus/', views.MenuView.as_view(), name='menu-list'),
    path('calculator/', views.Calculator.as_view(), name='calculator')
]
