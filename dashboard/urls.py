from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='Home'),
    path('staff',views.staff,name='dash-staff'),
    path('product',views.Product,name='dash-product'),
    path('order',views.Order,name='dash-order'),
]