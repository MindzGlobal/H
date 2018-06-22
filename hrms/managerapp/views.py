# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'manager/base_manager.html')

def index_manager(request):
    return render(request, 'manager/index_manager.html')

def holidays_manager(request):
    return render(request, 'manager/holidays_manager.html')

def employees_manager(request):
    return render(request, 'manager/employees_manager.html')

def attendance_manager(request):
    return render(request, 'manager/attendance_manager.html')

def designations_manager(request):
    return render(request, 'manager/designations_manager.html')

def leaves_manager(request):
    return render(request, 'manager/leaves_manager.html')

def leads_manager(request):
    return render(request, 'manager/leads_manager.html')

def salary_manager(request):
    return render(request, 'manager/salary_manager.html')

def salary_manager_emp(request):
    return render(request, 'manager/salary_manager_emp.html')

def salaryview_manager(request):
    return render(request, 'manager/salaryview_manager.html')

def sndmsg_manager(request):
    return render(request, 'manager/sndmsg_manager.html')

def mailview(request):
    return render(request, 'manager/mailview.html')

def addemployee(request):
    return render(request, 'manager/addemployee.html')

def profile_manager(request):
    return render(request, 'manager/profile_manager.html')

def editprofile_manager(request):
    return render(request, 'manager/editprofile_manager.html')

def changepwd_manager(request):
    return render(request, 'manager/changepwd_manager.html')

def login(request):
    return render(request, 'manager/login.html')

def register(request):
    return render(request, 'manager/register.html')

def forgot_pw(request):
    return render(request, 'manager/forgot-password.html')