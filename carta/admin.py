from django.contrib import admin

# Register your models here.
from carta.models import ProductoMenu


class ProductoMenuAdmin(admin.ModelAdmin):
    list_display = ('nombre_platillo', 'precio', 'categoria')


admin.site.register(ProductoMenu, ProductoMenuAdmin)