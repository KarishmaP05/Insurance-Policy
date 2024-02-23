from django.db import models
from datetime import date

# Create your models here.

class Customer(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Phone_No=models.IntegerField()
    Email_Id=models.CharField(max_length=100)
    City=models.CharField(max_length=50)
    Reference=models.CharField(max_length=50)
    Follow_up_date=models.DateField(default=date.today())
    Notes=models.CharField(max_length=1000)
    Customer_Type=models.CharField(max_length=50)
    Assign_to=models.CharField(max_length=50)

    def __str__(self):
        return self.FirstName


class Lead(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Phone_No=models.IntegerField()
    City=models.CharField(max_length=50)
    Reference=models.CharField(max_length=50)
    LOB=models.CharField(default='Engineering',max_length=50)
    Follow_up_date=models.DateField(default=date.today())
    Notes=models.CharField(max_length=1000)
    

    def __str__(self):
        return self.FirstName
