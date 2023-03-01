from django.contrib import admin
from django.contrib.auth.models import Group

from .models import product,order

class productview(admin.ModelAdmin):
    list_display=('name','category','quantity')
    list_filter=('category','quantity')

class orderview(admin.ModelAdmin):
    list_display=('product','order_quantity','date')

admin.site.site_header='Stock Admin'
admin.site.register(product,productview)
admin.site.register(order,orderview)
# admin.site.unregister(Group)
# Register your models here.
