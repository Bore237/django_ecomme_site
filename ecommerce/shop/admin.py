from django.contrib import admin

from .models import Category, Product, Commande
# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display= ('id', 'title', 'price', 'category', 'date_added')
    
class AdminCommande(admin.ModelAdmin):
    list_display= ('items', 'nom', 'email', 'ville', 'pays', 'total', 'zipcode')
    
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Commande, AdminCommande)