from django.urls import path


# from django.conf.urls import url
from . import views
app_name = 'InsurancePolicy'

urlpatterns = [
     path('',views.index, name="index" ),
    path('table/',views.table,name="table" ),
   
    

   
]