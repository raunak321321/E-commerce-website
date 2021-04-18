from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    # products  = Product.objects.all()
    allProds=[]
    catprods = Product.objects.values('category','id')
    #  iise hm category and id le rahe h catprods m 
    # cats = {item['category'] for item in catprods}
    # print(catprods)
    cats = set()
    for item in catprods:
        cats.add(item['category'])
        
    for cat in cats:
        prod = Product.objects.filter(category=cat) 
        # iska matlab h sirf vohi object do jinki category cat h
        n = len(prod)
        n_slides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,n_slides),n_slides])
    
    params = {"allProds" : allProds}
    # as we can pass only dictionary thats why we are writing like this 
    
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