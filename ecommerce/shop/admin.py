from django.contrib import admin

from .models import Category, Product, Commande
# Register your models here.

#Changer le nom de la bd
admin.site.site_header = "E-commerce"
admin.site.site_title = " Model Shop"
admin.site.index_title= "Manageur"



class AdminCategorie(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_added')

class AdminProduct(admin.ModelAdmin):
    list_display= ('id', 'title', 'price', 'category', 'date_added')
    #mettrer une bare de recherche
    search_fields = ('title','price')
    #Rendre  le chanps editable
    list_editable = ('price', )
    
    
class AdminCommande(admin.ModelAdmin):
    list_display= ('items', 'nom', 'email', 'ville', 'pays', 'total', 'zipcode')
    
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Commande, AdminCommande)