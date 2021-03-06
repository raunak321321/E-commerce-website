from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    sub_category = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300,default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to = "shop/images",default="")

    def __str__(self):
        return self.product_name  # search on google isse us product ka naam dikhega admin m wrna object1 and object 2 like that dikha raha tha


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=500,default="")
    
    def __str__(self):
        return self.name  # search on google isse us product ka naam dikhega admin m wrna object1 and object 2 like that dikha raha tha
# after this add to migrations via some command you know and then register this model in admin.py