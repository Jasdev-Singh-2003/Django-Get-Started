from django.contrib import admin
from .models import userModel, Product

# Register your models here.

admin.site.register(userModel)
admin.site.register(Product)
