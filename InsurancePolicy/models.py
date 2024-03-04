from django.db import models
from datetime import date
from django.conf import settings
from django.contrib.auth.models import User


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
    Customer_Id=models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
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
        return str(self.Customer_Id.FirstName)
    

class Claim(models.Model):
    Customer_Id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Policy_Id=models.ForeignKey(Policy,on_delete=models.CASCADE)
    Claim_Incident_Date=models.DateField(default=date.today())
    Claim_Filed_Date=models.DateField(default=date.today())
    Claim_Reason=models.CharField(max_length=500)
    Requested_Claim_Amount=models.IntegerField()
    Claim_Status=models.CharField(max_length=500)
    Claim_Final_Paid=models.IntegerField()
    Notes=models.CharField(max_length=500)
    

    def __str__(self):
        return str(self.Customer_Id)
    

class Employee(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Phone_No=models.IntegerField()
    Email_Id=models.CharField(max_length=100)
    Password=models.IntegerField()
    Gender=models.CharField(max_length=100)
    Job_Title=models.CharField(max_length=100)
    Job_Location=models.CharField(max_length=100)
    Joining_Date=models.DateField(default=date.today())
    Date_Of_Birth=models.DateField(default=date.today())

    def __str__(self):
            return self.FirstName
    


class User_Profile(models.Model):
    User_Id=models.ForeignKey(User,on_delete=models.CASCADE)
    LastName=models.CharField(max_length=50)
    Email_Id=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Date_of_Birth=models.DateField(default=date.today())
    Gender=models.CharField(max_length=50)
    FatherName=models.CharField(max_length=50)
    FatherDOB=models.DateField(default=date.today())
    MotherName=models.CharField(max_length=50)
    MotherDOB=models.DateField(default=date.today())
    MaritalStatus=models.CharField(max_length=50)
    LinkedIn=models.CharField(max_length=50)
    Twitter=models.CharField(max_length=50)
    Instagram=models.CharField(max_length=50)


    def __str__(self):
        return str(self.User_Id.username)



