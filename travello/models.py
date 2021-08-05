from django.db import models

# Create your models here.
class Food : 
    id : int 
    name : str
    img:str
    food:str
    price:int

class Student(models.Model):   
    roll = models.CharField(max_length=100)
    sclass = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    class Meta:
        db_table = "students"