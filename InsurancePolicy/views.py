from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from .models import Customer,Lead,Policy,Claim,Employee,User_Profile
from django.contrib.auth import logout
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request,'index.html',{})
    else:
        return redirect('/signin')
    
def leads(request):
    leads=Lead.objects.all()
    return render(request,'leads.html',{'leads':leads})

def customer(request):
    customers=Customer.objects.all()
    return render(request,'customer.html',{'customers':customers})

def signup(request):
    if request.method == 'POST':
        firstname=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']

        u = User.objects.create_user(username=email,email=email,first_name=firstname,password=password)
        user_profile=User_Profile.objects.create(User_Id=u,Email_Id=email)


        print(u)

        return redirect('/signin')
           
    return render(request,'signup.html',{})

def signin(request):
   
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user = authenticate(request, username=email, password=password)
        
        print("user",user)
        if user is not None:
         
            login(request, user)
            print("you have successfully login")
            return redirect('/')    # 

        else:
            
            print("Invalid Credentials")
            return redirect('/signin')  # url/action at the time of redirect
        

    return render(request,'signin.html',{})


def logout_user(request):
    logout(request)
    return redirect('/signin')

def error_page(request):
    return render(request,'404.html',{})

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
        city=request.POST['city']
        reference=request.POST['reference']
        lob=request.POST['lob']
        follow_up_date=request.POST['follow-up date']
        notes=request.POST['notes']
        
        add_lead=Lead.objects.create(FirstName=firstname,LastName=lastname,Phone_No=phoneno,City=city,Reference=reference,LOB=lob,Follow_up_date=follow_up_date,Notes=notes)
        return redirect('/leads')
    
    
    return render(request,'add_lead_form.html',{})



def edit_leads(request,id):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        phoneno=request.POST['phoneno']
        city=request.POST['city']
        reference=request.POST['reference']
        lob=request.POST['lob']
        follow_up_date=request.POST['follow-up date']
        notes=request.POST['notes']
        
        edit_lead=Lead.objects.get(id=id)
        edit_lead.FirstName=firstname
        edit_lead.LastName=lastname
        edit_lead.Phone_No=phoneno
        edit_lead.City=city
        edit_lead.Reference=reference
        edit_lead.LOB=lob
        edit_lead.Follow_up_date=follow_up_date
        edit_lead.Notes=notes
        edit_lead.save()
        return redirect('/leads')
    
    displaylead=Lead.objects.get(id=id)
    return render(request,'edit_lead.html',{'displaylead':displaylead})



def edit_customers(request,id):
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

        edit_customer=Customer.objects.get(id=id)
        edit_customer.FirstName=firstname
        edit_customer.LastName=lastname
        edit_customer.Phone_No=phoneno
        edit_customer.Email_Id=email_id
        edit_customer.City=city
        edit_customer.Reference=reference
        edit_customer.Follow_up_date=follow_up_date
        edit_customer.Notes=notes
        edit_customer.Customer_Type=customer_type
        edit_customer.Assign_to=assign_to
        edit_customer.save()

        return redirect('/customer')
    
    displaycustomer=Customer.objects.get(id=id)
    return render(request,'edit_customer.html',{'displaycustomer':displaycustomer})

def claims(request):
    claims=Claim.objects.all()

    return render(request,'claim.html',{'claims':claims})

def policy(request,id):
    policies=Policy.objects.filter(Customer_Id=id)
    return render(request,'policy.html',{'policies':policies})

def add_policy(request):
    if request.method=='POST':
        cust_id=request.POST.get('cust_id', False)
        cust_instance= Customer.objects.get(id=int(cust_id))
        start_date=request.POST['startdate']
        end_date=request.POST['enddate']
        insurance_type=request.POST['insurance-type']
        company=request.POST['company']
        lob=request.POST['lob']
        policy_number=request.POST['policynumber']
        product_name=request.POST['productname']
        sum_insured=request.POST['suminsured']
        od=request.POST['od']
        tp=request.POST['tp']
        gst_rate=request.POST['gst rate']
        gross_premium=request.POST.get('gross premium',False)
        net_premium=request.POST.get('net premium',False)
        attchment=request.POST['attachment']
        add_policy=Policy.objects.create(Customer_Id=cust_instance,Start_Date=start_date,End_Date=end_date,Insurance_Type=insurance_type,Company=company,LOB=lob,Policy_Number=policy_number,Product_Name=product_name,Sum_Insured=sum_insured,OD=od,TP=tp,GST_Rate=gst_rate,Gross_Premium=gross_premium,Net_Premium=net_premium,Attachment=attchment)
        return redirect('/policy')
    return render(request,'add_policy_form.html',{})

def edit_policy(request,id):
    if request.method=='POST':
        start_date=request.POST['startdate']
        end_date=request.POST['enddate']
        insurance_type=request.POST['insurance-type']
        company=request.POST['company']
        lob=request.POST['lob']
        policy_number=request.POST['policynumber']
        product_name=request.POST['productname']
        sum_insured=request.POST['suminsured']
        od=request.POST['od']
        tp=request.POST['tp']
        gst_rate=request.POST['gst rate']
        gross_premium=request.POST.get('gross premium',False)
        net_premium=request.POST.get('net premium',False)
        attchment=request.POST['attachment']

        edit_policy=Policy.objects.get(id=id)
        edit_policy.Start_Date=start_date
        edit_policy.End_Date=end_date
        edit_policy.Insurance_Type=insurance_type
        edit_policy.Company=company
        edit_policy.LOB=lob
        edit_policy.Policy_Number=policy_number
        edit_policy.Product_Name=product_name
        edit_policy.Sum_Insured=sum_insured
        edit_policy.OD=od
        edit_policy.TP=tp
        edit_policy.GST_Rate=gst_rate
        edit_policy.Gross_Premium=gross_premium
        edit_policy.Net_Premium=net_premium
        edit_policy.Attachment=attchment
        edit_policy.save()
        return redirect('/policy')
    

    displaypolicy=Policy.objects.get(id=id)
    return render(request,'edit_policy.html',{'displaypolicy':displaypolicy})


def create_claims(request):
    if request.method=='POST':
        cust_id=request.POST['cust_id']
        cust_instance= Customer.objects.get(id=int(cust_id))
        # cust_phone=request.POST['phoneno']
        # phone_instance=Customer.objects.get(id=int(cust_id))
        policy_id=request.POST['Policy_id']
        policy_instance=Policy.objects.get(id=int(policy_id))
        print("dfjhdfkjdgfkjdgfdk",policy_instance.LOB)   # It returns ID of that policy

        claim_incident_date=request.POST['claim_incident_date']
        claim_filed_date=request.POST['claim_filed_date']
        claim_reason=request.POST['claim_reason']
        requested_claim_amount=request.POST['requested_claim_amount']
        claim_status=request.POST['claim_status']
        claim_final_paid=request.POST['claim_final_paid']
        notes=request.POST['notes']
        create_claim=Claim.objects.create(Customer_Id=cust_instance,Policy_Id=policy_instance,Claim_Incident_Date=claim_incident_date,Claim_Filed_Date=claim_filed_date,Claim_Reason=claim_reason,Requested_Claim_Amount=requested_claim_amount,Claim_Status=claim_status,Claim_Final_Paid=claim_final_paid,Notes=notes)

        return redirect('/claims')

    customers=Customer.objects.all()
    policies=Policy.objects.all()
    return render(request,'create_claim_form.html',{'customers':customers,'policies':policies})




def profile(request):
    update_user=User_Profile.objects.get(User_Id=request.user.id)
    print("############",update_user)
    return render(request,'profile.html',{'update_user':update_user})

def family_details(request):
    update_user=User_Profile.objects.get(User_Id=request.user.id)
    return render(request,'familydetails.html',{'update_user':update_user})


def social_media(request):
    update_user=User_Profile.objects.get(User_Id=request.user.id)
    return render(request,'socialmedia.html',{'update_user':update_user})



def team(request):
    employees=Employee.objects.all()
    return render(request,'team.html',{'employees':employees})

def add_employee(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        phoneno=request.POST['phoneno']
        email_id=request.POST['email']
        password=request.POST['password']
        gender=request.POST['gender']
        job_title=request.POST['job-title']
        job_location=request.POST['job-location']
        joining_date=request.POST['joining-date']
        date_of_birth=request.POST['dob']
        add_employee=Employee.objects.create(FirstName=firstname,LastName=lastname,Phone_No=phoneno,Email_Id=email_id,Password=password,Gender=gender,Job_Title=job_title,Job_Location=job_location,Joining_Date=joining_date,Date_Of_Birth=date_of_birth)
        return redirect('/team')

    return render(request,'add_employee_form.html',{})


def single_view(request):

    return render(request,'single_view_of_customer.html',{})


def save_profile(request):
    if request.method=='POST':
        save_type=request.POST['save_type']
       

        if save_type=='personal_details':
            firstname = request.POST['firstName']
            lastname=request.POST['lastName']
            email_id=request.POST['email']
            address=request.POST['address']
            date_of_birth=request.POST['dob']
            gender=request.POST['gender']
          

            save_profile=User_Profile.objects.get(User_Id=request.user.id)
            
            save_profile.User_Id.username=firstname
            save_profile.LastName=lastname
            save_profile.Email_Id=email_id
            save_profile.Address=address
            save_profile.Date_of_Birth=date_of_birth
            save_profile.Gender=gender
            save_profile.save()

        if save_type=='family_details':

            
            fathername=request.POST['fatherName']
            mothername=request.POST['motherName']
            fatherDOB=request.POST['fatherDOB']
            motherDOB=request.POST['motherDOB']
            maritalstatus=request.POST['maritalstatus']

            save_profile=User_Profile.objects.get(User_Id=request.user.id)
            save_profile.FatherName=fathername
            save_profile.FatherDOB=fatherDOB
            save_profile.MotherName=mothername
            save_profile.MotherDOB=motherDOB
            save_profile.MaritalStatus=maritalstatus
            save_profile.save()



        if save_type=='social_media':

     
            linkedin=request.POST['linkedin']
            twitter=request.POST['twitter']
            instagram=request.POST['instagram']
            save_profile=User_Profile.objects.get(User_Id=request.user.id)
            save_profile.LinkedIn=linkedin
            save_profile.Instagram=instagram
            save_profile.Twitter=twitter
            save_profile.save()

        return redirect('/profile')
    
   
    return render(request,'profile.html',{})



   