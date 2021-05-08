from django.db import models
from django.conf import settings


# Create your models here.


class Customer(models.Model):
    customer = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    customer_username = models.CharField(max_length=30, blank=False, null=False)
    customer_mobile_number = models.IntegerField(unique=True,null=False,blank=False)
    customer_address = models.CharField(max_length=200, blank=True, null=True)



class Store(models.Model):
    store_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100, blank=False, null=False)
    store_address = models.CharField(max_length=500, blank=True, null=True)
    store_link = models.URLField(blank=False, null=False)
    
    def __str__(self):
        return self.store_name

class Category(models.Model):
    product_category = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.product_category

class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=False, null=False)
    product_description = models.CharField(max_length=1000, blank=True, null=True)
    product_mrp = models.DecimalField(default= 0.00, max_digits=18, decimal_places=2)
    product_sprice = models.DecimalField(default= 0.00, max_digits=18, decimal_places=2)
    product_image = models.URLField(blank=True, null=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, blank=False, null=False)
    store = models.OneToOneField(Store, on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False, default=1)
    ordered = models.BooleanField(default=False)


    def get_total_item_price(self):
        return self.orderitem_quantity * self.product.product_sprice
    

    def __str__(self):
        return self.product.product_name 



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(OrderItem)
    order_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def get_total_price(self):
        total = 0
        for order_item in self.order_items.all():
            total += order_item.get_total_item_price()
        return total


    def __str__(self):
        return self.id