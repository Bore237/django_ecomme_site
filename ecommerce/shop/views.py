from django.shortcuts import render
from .models import Product 
# Create your views here.

def index (request):
    product_object = Product.objects.all()
    return render(request, 'shop/index.html', {'product_object' : product_object})