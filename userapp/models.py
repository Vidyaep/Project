from django.db import models

# Create your models here.


class Education(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    


class Profile(models.Model):
    educcation = models.ManyToManyField(Education)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
