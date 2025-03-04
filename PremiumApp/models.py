from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm,TextInput,NumberInput,EmailInput
# Create your models here.


class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    description = RichTextUploadingField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    fax = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True, null=True, max_length=50)
    smptserver = models.CharField(max_length=100)
    smtpemail = models.EmailField(blank=True, null=True,max_length=50)
    smptpassword = models.CharField(blank=True, max_length=50)
    smptport = models.CharField(blank=True, max_length=100)
    icon=models.ImageField(blank=True, null=True,upload_to='icon/')
    facebook = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    address = RichTextUploadingField()
    contact = RichTextUploadingField()
    reference = RichTextUploadingField()
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class ContactMessage(models.Model):
    STATUS = (
('New','New'),
('Read','Read'),
('Closed','Closed'),

        )
    name= models.CharField(max_length=200)
    email=models.EmailField(max_length=40)
    subject=models.CharField(max_length=200,blank=True)
    message=models.CharField(max_length=500, blank=True)
    status=models.CharField(max_length=40,choices=STATUS,default='New')
    ip=models.CharField(max_length=100,blank=True)
    Note=models.CharField(max_length=200, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name



class ContactForm(ModelForm):
    class Meta:
        model=ContactMessage
        fields=['name','email','subject','message']
        widgets={
        'name':TextInput(attrs={'class':'input','placeholder':'Name & Sure name'}),
        'email':EmailInput(attrs={'class':'input','placeholder':'Write your email'}),
        'subject':TextInput(attrs={'class':'input','placeholder':'Wrte your Subjects'}),
        'message':TextInput(attrs={'class':'input','placeholder':'Write your messages'}),
        }