from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'categorys'

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    crated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'  