
from django.urls import path
from PremiumApp.views import index,contact,AboutUS,category_element,product_detail,add_to_cart,SearchView,search_auto,Comment_Add
#app_name='PremiumApp'

urlpatterns = [
path('',index,name='index' ),
path('about/',AboutUS,name='AdminAbout'),
path('contact/',contact, name='contact'),
path('category/<int:id>/<slug:slug>/', category_element,name='category_element'),
path('product_detail/<int:id>/<slug:slug>/', product_detail,name='product_details'),
path('product_cart/<int:id>/', add_to_cart,name='add_to_c'),
path('search/',SearchView,name='SearchView' ),
path('search_auto/', search_auto,name="search_auto"),
path('comment_add/<int:id>/',Comment_Add,name='comment_add' )


]
