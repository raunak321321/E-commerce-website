from django.shortcuts import render
from django.http import HttpResponse
from .models import Product , Contact
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
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        # where first name is which is in models and second one is in our if statements
        contact.save()
    return render(request,'shop/contact.html')
def tracker(request):
    return render(request,'shop/tracker.html')
def search(request):
    return render(request,'shop/search.html')
def ProductView(request,myid):
    # we are fetching id here
    product = Product.objects.filter(id=myid) 
    # here product is a list
    return render(request,'shop/prodview.html',{"product":product[0]})#here we write 0 because we want fetch the product in the list and as there is only one in the list so we can fetch it via 0.
def checkout(request): 
    return render(request,'shop/checkout.html')