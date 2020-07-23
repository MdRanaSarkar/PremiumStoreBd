
from django.urls import path
from Order.views import Add_to_Shoping_cart,Cart_details,ShopcartDelete,OrderCart

urlpatterns=[
path('addingcart/<int:id>/', Add_to_Shoping_cart,name='Add_to_Shoping_cart'),
path('cart_details/', Cart_details,name="Cart_details"),
path('delete_cart/<int:id>/',ShopcartDelete,name="ShopcartDelete"),
path('oder_cart/',OrderCart,name="OrderCart"),


]