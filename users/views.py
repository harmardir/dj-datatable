from django.shortcuts import render, redirect  

from users.models import Employee  

def index(request):  
    employees = Employee.objects.all()  
    return render(request,"dashboard.html",{'employees':employees})  
