from django.contrib import admin
from .models import Customer ,Lead, Policy,Claim,Employee,User_Profile

# Register your models here.
admin.site.register(Customer)
admin.site.register(Lead)
admin.site.register(Policy)
admin.site.register(Claim)
admin.site.register(Employee)
admin.site.register(User_Profile)