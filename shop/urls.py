# I made this file
from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="ShopHome"),
    path('about/', views.about,name="AboutUs"),
    path('contact/', views.contact,name="ContactUs"),
    path('tracker/', views.tracker,name="TrackingStatus"),
    path('search/', views.search,name="Search"),
    path('products/<int:myid>', views.ProductView,name="ProductView"),#Here we are giving arguments to function which we are calling 
    path('checkout/', views.checkout,name="Checkout") 
]
