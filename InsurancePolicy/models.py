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
    STATUS_CHOICES = (
         
         
        ("active", 'active'),
        ("inactive", 'inactive'),
    )
    Lead_Status=models.CharField(max_length=50,choices=STATUS_CHOICES, default="active")
    

    def __str__(self):
        return self.FirstName

class Policy(models.Model):
    Start_Date=models.DateField(default=date.today())
    End_Date=models.DateField(default=date.today())
    Insurance_Type=models.CharField(max_length=50)
    Company=models.CharField(max_length=50)
    LOB=models.CharField(default='Engineering',max_length=50)
    Policy_Number=models.IntegerField()
    Product_Name=models.CharField(max_length=50)
    Sum_Insured=models.IntegerField()
    OD=models.IntegerField()
    TP=models.IntegerField()   
    GST_Rate=models.IntegerField() 
    Gross_Premium=models.IntegerField()
    Net_Premium=models.IntegerField()
    Attachment=models.FileField(upload_to='pdfs/', null=True, blank=True)
    

    STATUS_CHOICES = (
         
         
        ("active", 'active'),
        ("inactive", 'inactive'),
    )
    Policy_Status=models.CharField(max_length=50,choices=STATUS_CHOICES, default="active")

  
    
    def __str__(self):
        return str(self.Policy_Number)