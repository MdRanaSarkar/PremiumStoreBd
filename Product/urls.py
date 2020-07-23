from django.urls import  path

from Product.views import Product_Index

urlpatterns=[

path('',Product_Index,name='Product_Index'),

]