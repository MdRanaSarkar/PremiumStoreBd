from django.contrib import admin

# Register your models here.
from PremiumApp.models import Setting,ContactForm,ContactMessage

class SettingAdmin(admin.ModelAdmin):
	list_display = ['title','created_at','updated_at']
	list_filter = ['phone','created_at','updated_at']
	search_fields = ['title','keyword','description','phone','fax','email','address','contact','reference']


admin.site.register(Setting, SettingAdmin)


class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ['name','created_at','updated_at']

admin.site.register(ContactMessage,ContactMessageAdmin)
