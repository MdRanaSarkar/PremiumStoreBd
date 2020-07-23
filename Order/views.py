from django.shortcuts import render

from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,reverse
# Create your views here.
from Order.models import ShopingCart,ShopingCartForm,OderForm,Order,OderProduct
from Product.models import Category,Product,Images,Comment,CommenttForm
from django.contrib import messages
from user.models import UserProfile
from django.utils.crypto import get_random_string
def Add_to_Shoping_cart(request,id):
	url=request.META.get('HTTP_REFERER')
	current_user=request.user
	checking=ShopingCart.objects.filter(product_id=id,user_id=current_user.id)
	if checking:
		control=1
	else:
		control=0

	if request.method=="POST":
		form =ShopingCartForm(request.POST)
		if form.is_valid():
			if control==1:
				data=ShopingCart.objects.filter(product_id=id, user_id=current_user.id)
				data.quantity+=form.cleaned_data['quantity']
				data.save()
			else:
				data=ShopingCart()
				data.user_id=current_user.id
				data.product_id=id
				data.quantity=form.cleaned_data['quantity']
				data.save()
		messages.success(request, 'Your Product  has been added')
		return HttpResponseRedirect(url)
	else:
		if control ==1:
			data=ShopingCart.objects.filter(product_id=id, user_id=current_user.id)
			data.quantity+=1
			data.save()
		else:
			data=ShopingCart()
			data.user_id=current_user.id
			data.product_id=id
			data.quantity=1
			data.save()
		messages.success(request,'Your  product has been added')
		return HttpResponseRedirect(url)


#@login_required(login_url='/login')
def Cart_details(request):
	category=Category.objects.all()
	current_user=request.user
	shoping_cart=ShopingCart.objects.filter(user_id=current_user.id)
	totalamount=0
	for rs in shoping_cart:
		totalamount+=rs.quantity*rs.product.new_price
	counting_product=0
	for p in shoping_cart:
		counting_product+=rs.quantity
	context={
	'category':category,
	'shoping_cart':shoping_cart,
	'totalamount':totalamount,
	'counting_product':counting_product

	}
	return render(request, 'cart_detials.html',context)

def ShopcartDelete(request,id):
	ShopingCart.objects.filter(id=id).delete()
	messages.success(request, 'Your informative Your added cart is deleted')
	return HttpResponseRedirect(reverse('Cart_details'))




def  OrderCart(request):
	category=Category.objects.all()
	current_user=request.user
	shoping_cart=ShopingCart.objects.filter(user_id=current_user.id)
	totalamount=0
	for rs in shoping_cart:
		totalamount+=rs.quantity*rs.product.new_price
	if request.method=="POST":
		form=OderForm(request.POST)
		if form.is_valid():
			dat = Order()
			dat.first_name = form.cleaned_data['first_name'] #get product quantity from form
			dat.last_name = form.cleaned_data['last_name']
			dat.address = form.cleaned_data['address']
			dat.city = form.cleaned_data['city']
			dat.phone = form.cleaned_data['phone']
			dat.user_id = current_user.id
			dat.total = totalamount
			dat.ip = request.META.get('REMOTE_ADDR')
			ordercode= get_random_string(5).upper() # random cod
			dat.code =  ordercode
			dat.save() #



			#moving data shortcart to product cart
			for rs in shoping_cart:
				data=OderProduct()
				data.order_id=dat.id
				data.product_id=rs.product_id
				data.user_id=current_user.id
				data.quantity=rs.quantity
				data.price=rs.product.new_price
				data.amount=rs.total_amount
				data.save()

				product = Product.objects.get(id=rs.product_id)
				product.amount -= rs.quantity
				product.save()
			#Now remove all oder data from the shoping cart
			ShopingCart.objects.filter(user_id=current_user.id).delete()
			#request.session['cart_item']=0
			messages.success(request,'Your oder has been completed')
			context={
			'category':category,
			'ordercode':ordercode,
			}
		
			return render(request, 'oder_completed.html',context)
		else:
			messages.warning(request, form.errors)
			return HttpResponseRedirect("/order/oder_cart")
	form=OderForm()
	profile=UserProfile.objects.get(user_id=current_user.id)
	context={
	'category':category,
	'shoping_cart':shoping_cart,
	'totalamount':totalamount,
	'profile':profile,
	'form':form,
	}
	return render(request, 'order_form.html',context)
