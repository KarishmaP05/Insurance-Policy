from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from .models import Customer,Lead

# Create your views here.

def index(request):
    return render(request,'index.html',{})
def leads(request):
    return render(request,'leads.html',{})

def customer(request):
    customers=Customer.objects.all()
    return render(request,'customer.html',{'customers':customers})

def signup(request):
    if request.method == 'POST':
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']

        u = User.objects.create_user(username=username,email=email,password=password)

        print(u)

        return redirect('/signin')
           
    return render(request,'signup.html',{})

def signin(request):
    return render(request,'signin.html',{})

def table(request):
    return render(request,'table.html',{})

def form(request):
    return render(request,'form.html',{})

def add_customers(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        phoneno=request.POST['phoneno']
        email_id=request.POST['email']
        city=request.POST['email']
        reference=request.POST['reference']
        follow_up_date=request.POST['follow-up date']
        notes=request.POST['notes']
        customer_type=request.POST['customer-type']
        assign_to=request.POST.get('assign_to',False);
        add_customer=Customer.objects.create(FirstName=firstname,LastName=lastname,Phone_No=phoneno,Email_Id=email_id,City=city,Reference=reference,Follow_up_date=follow_up_date,Notes=notes,Customer_Type=customer_type,Assign_to=assign_to)
        return redirect('/customer')
    return render(request,'add_customer_form.html',{})

def add_leads(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        phoneno=request.POST['phoneno']
        email_id=request.POST['email']
        city=request.POST['email']
        reference=request.POST['reference']
        follow_up_date=request.POST['follow-up date']
        notes=request.POST['notes']
        customer_type=request.POST['customer-type']
        assign_to=request.POST.get('assign_to',False);
        add_customer=Lead.objects.create(FirstName=firstname,LastName=lastname,Phone_No=phoneno,Email_Id=email_id,City=city,Reference=reference,Follow_up_date=follow_up_date,Notes=notes,Customer_Type=customer_type,Assign_to=assign_to)
        return redirect('/leads')
    
    
    return render(request,'add_lead_form.html',{})






