from django.db import models

# Create your models here.

class ThaiFood(models.Model):
    FoodTypes = models.CharField(max_length=50)
    FoodTitle = models.CharField(max_length=100)
    FoodSubTitle = models.CharField(max_length=120)
    FoodPrice = models.IntegerField()
    FoodDesc = models.CharField(max_length=150)
    FoodImage = models.ImageField(upload_to="img/")
    def __str__(self):
        return self.FoodTypes
    
class IndianFood(models.Model):
    FoodTypes = models.CharField(max_length=50)
    FoodTitle = models.CharField(max_length=100)
    FoodSubTitle = models.CharField(max_length=120)
    FoodPrice = models.IntegerField()
    FoodDesc = models.CharField(max_length=150)
    FoodImage = models.ImageField(upload_to="img/")
    def __str__(self):
        return self.FoodTypes

class DumplingsFood(models.Model):
    FoodTypes = models.CharField(max_length=50)
    FoodTitle = models.CharField(max_length=100)
    FoodSubTitle = models.CharField(max_length=120)
    FoodPrice = models.IntegerField()
    FoodDesc = models.CharField(max_length=150)
    FoodImage = models.ImageField(upload_to="img/")
    def __str__(self):
        return self.FoodTypes

class ContinentalFood(models.Model):
    FoodTypes = models.CharField(max_length=50)
    FoodTitle = models.CharField(max_length=100)
    FoodSubTitle = models.CharField(max_length=120)
    FoodPrice = models.IntegerField()
    FoodDesc = models.CharField(max_length=150)
    FoodImage = models.ImageField(upload_to="img/")
    def __str__(self):
        return self.FoodTypes

class Book_A_Table(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    people = models.CharField(max_length=50)
    messagess = models.CharField(max_length=300) 
    def __str__(self):
        return self.name
class qualification(models.Model):
    Name = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    rate = models.IntegerField()
    messagesss = models.CharField(max_length=300)
    def __str__(self):
        return self.Name
        
    

    
    

    
