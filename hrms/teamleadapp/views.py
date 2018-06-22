# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.

def home_teamlead(request):
    return render(request, 'teamlead/base_teamlead.html')

def index_teamlead(request):
    return render(request, 'teamlead/index_teamlead.html')

def holidays_teamlead(request):
    return render(request, 'teamlead/holidays_teamlead.html')

def attendance_teamlead(request):
    return render(request, 'teamlead/attendance_teamlead.html')

def salary_teamlead(request):
    return render(request, 'teamlead/salary_teamlead.html')

def salaryview_teamlead(request):
    return render(request, 'teamlead/salaryview_teamlead.html')

def profile_teamlead(request):
    return render(request, 'teamlead/profile_teamlead.html')

def editprofile_teamlead(request):
    return render(request, 'teamlead/editprofile_teamlead.html')

def changepwd_teamlead(request):
    return render(request, 'teamlead/changepwd_teamlead.html')

def leave_teamlead(request):
    return render(request, 'teamlead/leave_teamlead.html')

def compose_teamlead(request):
    return render(request, 'teamlead/compose_teamlead.html')

def mailview_teamlead(request):
    return render(request, 'teamlead/mailview_teamlead.html')

def employee_teamlead(request):
    return render(request, 'teamlead/employee_teamlead.html')