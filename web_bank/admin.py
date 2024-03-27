from django.contrib import admin
from .models import Product, Client

# Register your models here.

# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Client)
admin.site.register(Product)