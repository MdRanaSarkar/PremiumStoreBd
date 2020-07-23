from django.db import models

# Create your models here.
from Product.models import Product,Category
from django.contrib.auth.models import User
from django.forms import ModelForm


class ShopingCart(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
	user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	#variant = models.ForeignKey(Variants, on_delete=models.SET_NULL,blank=True, null=True)
	quantity = models.IntegerField()

	def __str__(self):
		return self.product.title


	@property
	def price(self):
		return (self.product.new_price)

	@property
	def total_amount(self):
		return (self.product.new_price*self.quantity)
		"""
	@property
	def varamount(self):
		return (self.quantity * self.variant.price) """

class ShopingCartForm(ModelForm):
	class Meta:
		model=ShopingCart
		fields=['quantity']


class  Order(models.Model):
	STATUS=(
		('New','New'),
		('Accepted','Accepted'),
		('Preparing','Preparing'),
		('Onshiping','Onshiping'),
		('Completed','Completed'),
		('Cancelled','Cancelled')
		)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	first_name=models.CharField(max_length=200)
	last_name=models.CharField(max_length=200)
	code=models.CharField(max_length=200,editable=False)
	phone=models.CharField(max_length=200,blank=True)
	address=models.CharField(max_length=200,blank=True)
	city=models.CharField(max_length=200)
	country=models.CharField(max_length=200,blank=True)
	total=models.FloatField()
	status=models.CharField(choices=STATUS,max_length=20,default='New')
	ip=models.CharField(max_length=200,blank=True)
	adminnote=models.CharField(max_length=200,blank=True)
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.first_name

class OderForm(ModelForm):
	class Meta:
		model=Order
		fields=['first_name','last_name','phone','address','city','country']


class OderProduct(models.Model):
	STATUS=(
		('New','New'),
		('Accepted','Accepted'),
		('Cancelled','Cancelled')
		)
	order=models.ForeignKey(Order, on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	product=models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity=models.IntegerField()
	price=models.FloatField()
	amount=models.FloatField()
	status= models.CharField(max_length=20,choices=STATUS,default='New')
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.product.title
