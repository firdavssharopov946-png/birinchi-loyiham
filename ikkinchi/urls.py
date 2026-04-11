from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('buyurtmalar/', views.buyurtmalar, name='buyurtmalar'),
    path('mahsulotlar/', views.mahsulotlar, name='mahsulotlar'),
    path('mijozlar/', views.mijozlar, name='mijozlar'),
    path('mahsulot-qoshish/', views.mahsulot_qoshish, name='mahsulot_qoshish'),
    path('buyurtma-qoshish/', views.buyurtma_qoshish, name='buyurtma_qoshish'),
    path('mijoz-qoshish/', views.mijoz_qoshish, name='mijoz_qoshish'),
    path('buyurtmalar/', views.buyurtmalar_list, name='buyurtmalar_list'),
]