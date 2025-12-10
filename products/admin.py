from django.contrib import admin
from . import models




class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","precio","stock")

class OfferAdmin(admin.ModelAdmin):
    list_display = ("codigo","descuento","descripcion")

admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Offer,OfferAdmin)


# Register your models here.
