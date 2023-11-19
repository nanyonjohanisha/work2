from django.db import models

#create your model here

class EquipmentCategory(models.Model):
    Category_id=models.AutoField(primary_key=True)
    Category_name=models.CharField(Unique=True,max_length=True)
    Category_description=models.TextField(blank=True)
    date_created=models.DateField(auto_now=True)
    
class Meta:
    Verbose_name_plural="Equipment Categories"
    def __str__(self):
        return self.Category_name
 
class Product (models.Model):
    product_id= models.IntegerField(Default=0)
    Category_id=models.ForeignKey('Category', on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200,)
    unit_price=models.IntegerField(max_length=120,)
    sale_price=models.IntegerField(max_length=20,)
    available_stock=models.IntegerField(max_length=100,)
    unit_measure=models.CharField(max_length=100,null=True)
    date_update=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product

class Transaction (models.Models):
   Transaction_id=models.IntegerField(max_length=150,null=True)
   product_id=models.ForeignKey('Product',on_delete=models.CASCADE)
   Transaction_type=models.CharField(max_length=660)
   stock_taken=models.IntegerField(max_length=100,null=True)
   transaction_amount=models.IntegerField(max_length=100,null=True)
   transaction_date=models.DateTimeField('date publishe')
   def __str__(self):
        return self.Transaction


