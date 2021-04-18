from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    # products  = Product.objects.all()
    allProds=[]
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        n_slides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,n_slides),n_slides])
    
    params = {"allProds" : allProds}
    
    return render(request,'shop/index.html',params)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return HttpResponse("We are at contact")
def tracker(request):
    return HttpResponse("We are at tracker")
def search(request):
    return HttpResponse("We are at search")
def ProdView(request):
    return HttpResponse("We are at product view")
def checkout(request):
    return HttpResponse("We are at checkout")