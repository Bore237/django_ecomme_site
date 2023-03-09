from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 200)
    date_added = models.DateTimeField(auto_now=True)
    
    #Faire que le nouveau element saisie est en tête
    class Meta:
        ordering = ['-date_added']
        
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length= 200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='categorie', on_delete= models.CASCADE)
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)
    
    #classer les produit par ordre d'ajout
    class Meta:
        ordering = ['-date_added']
        
    def __str__(self):
        return self.title