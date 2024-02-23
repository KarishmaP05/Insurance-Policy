from django.urls import path


# from django.conf.urls import url
from . import views
app_name = 'InsurancePolicy'

urlpatterns = [
    path('',views.index, name="index" ),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('leads/',views.leads,name='leads'),
    path('customer/',views.customer,name='customer'),
    path('table/',views.table,name='table'),
    path('form/',views.form,name="form"),
    path('add-customers/',views.add_customers,name='add-customers'),
    path('add-leads/',views.add_leads,name="add-leads")

    
   
   
]