from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    
    def __str__(self):
        return self.username
    

class CategoryModel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class SalesModel(models.Model):
    product_name = models.CharField(max_length=200, null=True, blank=True)
    
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name='category_info',
        null=True,
        blank=True
        )
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    tax_percent = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    total_price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    sale_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name
    
