
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,reverse
from django.contrib import messages
from django import forms
# Create your views here.
from PremiumApp.models import Setting,ContactForm,ContactMessage
from Product.models import Category,Product,Images,Comment,CommenttForm
from Product.forms import SearchForm
from django.db.models import Q
import json
def index(request):
	setting=Setting.objects.get(pk=1)
	category=Category.objects.all()
	slider_show=Product.objects.all().order_by('id')[:4]
	latest_product=Product.objects.all().order_by('-id')[:5]
	picked_product=Product.objects.all().order_by('?')[:4]
	page='index'

	context={
	'setting':setting,
	'page':page,
	'category':category,
	'slider_show':slider_show,
	'latest_product':latest_product,
	'picked_product':picked_product,

	}
	return render(request,'index.html',context)



def contact(request):
	if request.method=='POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			data=ContactMessage()
			data.name= form.cleaned_data['name']
			data.email=form.cleaned_data['email']
			data.subject=form.cleaned_data['subject']
			data.message =form.cleaned_data['message']
			data.ip=request.META.get('REMOTE_ADDR')
			data.save()
			messages.success(request, 'Your message has been sent')

			return HttpResponseRedirect(reverse('contact'))


	setting = Setting.objects.get(pk=1)
	form=ContactForm
	category=Category.objects.all()
	context={
	'setting':setting,'form':form,'category':category,
	}
	return render(request,'contact.html',context)

def AboutUS(request):
	setting = Setting.objects.get(pk=1)
	context={
	'setting':setting
	}
	return render(request,'About.html', context)


def category_element(request,id,slug):
	category=Category.objects.all()
	product=Product.objects.filter(category_id=id)
	context={
	'category':category,
	'product':product,

	}
	return render(request, 'category_product.html',context)


def product_detail(request,id,slug):
	category=Category.objects.all()
	product=Product.objects.get(pk=id)
	images=Images.objects.filter(product_id=id)
	picked_product=Product.objects.all().order_by('?')[:4]
	#it showing for comment
	comment_all=Comment.objects.filter(product_id=id,status='True')
	context={
	'category':category,
	'product':product,
	'images':images,
	'picked_product':picked_product,
	'comment_all':comment_all,

	}
	return render(request, 'product_details.html',context)
	



def Cart_details(request,id):
	category=Category.objects.all()
	product=Product.objects.get(pk=id)




















def add_to_cart(request,id):
	product_cart=Product.objects.filter(id=id)
	return HttpResponse(product_cart)



def SearchView(request):
	if request.method == 'POST':
		form=SearchForm(request.POST)
		if form.is_valid():
			query=form.cleaned_data['query']
			cat_id=form.cleaned_data['cat_id']
			if cat_id==0:
				products=Product.objects.filter(title__icontains=query)
			else:
				products=Product.objects.filter(title__icontains=query,category_id=cat_id)
			category=Category.objects.all()
			context={
			'category':category,
			'query':query,
			'products':products
			}
			return render(request, 'product_search.html',context)
	return HttpResponseRedirect('/')

...

def search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    products = Product.objects.filter(title__icontains=q)
    results = []
    for rana in products:
      product_json = {}
      product_json =rana.title
      results.append(product_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)






  #For 	PRODUCT COMMENT INDIVIDUALLY 
def Comment_Add(request,id):
	url=request.META.get('HTTP_REFERER')
	if request.method=='POST':
		pos=CommenttForm(request.POST)
		if pos.is_valid():
			data=Comment()
			data.subject=pos.cleaned_data['subject']
			data.comment=pos.cleaned_data['comment']
			data.rate=pos.cleaned_data['rate']
			data.ip=request.META.get('REMOTE_ADDR')
			data.product_id=id
			current_user=request.user
			data.user_id = current_user.id
			data.save()
			messages.success(request, 'Your informative comment has been sent')
			return HttpResponseRedirect(url)
	return HttpResponseRedirect(url)


