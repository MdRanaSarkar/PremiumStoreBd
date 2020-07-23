from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.


class Category(MPTTModel):
	status = (
		('True', 'True'),
		('False', 'False'),
	)
	parent =TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	title = models.CharField(max_length=200)
	keywords = models.CharField(max_length=100)
	image = models.ImageField(blank=True, upload_to='category/')
	status = models.CharField(max_length=20, choices=status)
	slug = models.SlugField(null=True,unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		full_path=[self.title]
		k=self.parent
		while k is not None:
			full_path.append(k.title)
			k=k.parent
		return '/'.join(full_path[::-1])

	def  image_tag(self):
		return mark_safe('<img src="{}" heights="50" />'.format(self.image.url))
	class MPTTMeta:
		order_insertion_by = ['title']
	def get_absolute_url(self):
		return reverse('category_element',kwargs={'slug':self.slug})



class Product(models.Model):
	status = (
		('True', 'True'),
		('False', 'False'),)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	keywords = models.CharField(max_length=100)
	image = models.ImageField(blank=True, upload_to='product/')
	new_price = models.DecimalField(decimal_places=2, max_digits=15,default=0)
	old_price = models.DecimalField(decimal_places=2, max_digits=15)
	amount = models.IntegerField(default=0)
	min_amount = models.IntegerField(default=3)
	detail = RichTextUploadingField()
	status = models.CharField(max_length=20, choices=status)
	slug = models.SlugField(null=True,unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
	def  image_tag(self):
		return mark_safe('<img src="{}" heights="50" width="40" />'.format(self.image.url))
	image_tag.short_description='Image'
	def get_absolute_url(self):
		return reverse('category_element',kwargs={'slug':self.slug})
	def imageurl(self):
		if self.image:
			return self.image.url
		else:
			return " "

class Images(models.Model):
	product =models.ForeignKey(Product,on_delete=models.CASCADE)
	title = models.CharField(max_length=200,blank=True)
	image=models.ImageField(blank=True, upload_to='product/')

	def __str(self):
		return self.title

	def imageurl(self):
		if self.image:
			return self.image.url


class Comment(models.Model):
	STATUS = (
('New','New'),
('True','True'),
('False','False'),

		)
	product=models.ForeignKey(Product, on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	subject=models.CharField(max_length=200,blank=True)
	comment=models.CharField(max_length=500, blank=True)
	rate=models.IntegerField(default=1)
	ip=models.CharField(max_length=100,blank=True)
	status=models.CharField(max_length=40,choices=STATUS,default='New')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.subject

class CommenttForm(ModelForm):
	class Meta:
		model=Comment
		fields=['subject','comment','rate']
