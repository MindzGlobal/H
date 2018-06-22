# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from .forms import addemployeeform
from .models import auth_user_extended,personnel_info,educational_info,experience_info
from django.contrib.auth.models import User
from django.http import HttpResponse
#
# # Create your views here.
# def insert(request):
#     user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')


def home(request):
    return render(request, 'hr/base.html')

def index(request):
    return render(request, 'hr/index.html')

def holidays(request):
    return render(request, 'hr/holidays.html')

def employees(request):
    return render(request, 'hr/employees.html')

def attendance(request):
    return render(request, 'hr/attendance.html')

def departments(request):
    return render(request, 'hr/departments.html')

def designations(request):
    return render(request, 'hr/designations.html')

def leaves(request):
    return render(request, 'hr/leaves.html')

def sndmsg_hr(request):
    return render(request, 'hr/sndmsg_hr.html')

def viewmsg_hr(request):
    return render(request, 'hr/viewmsg_hr.html')

def leads(request):
    return render(request, 'hr/leads.html')

def salary(request):
    return render(request, 'hr/salary.html')

def salary_hr(request):
    return render(request, 'hr/salary_hr.html')

def salary_emp(request):
    return render(request, 'hr/salary_emp.html')

def salaryview(request):
    return render(request, 'hr/salaryview.html')

# def addemployee(request):
#     if request.method == 'POST':
#         form = addemployeeform(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request, 'hr/index.html')
#     form = addemployeeform(request.POST, request.FILES)
#     return render(request, 'hr/addemployee.html', {'form': form})

def addemployee(request):
    return render(request, 'hr/addemployee.html')

def addempdetail(request):
    user = User(first_name=request.POST['name'],
                email=request.POST['email'],
                username=request.POST['username'],
                add_skill=request.POST['add_skill'])
    # addemp = auth_user_extended(is_role=request.POST['is_role'],
    #                             is_designation=request.POST['is_designation'],
    #                             profile_image=request.FILES['profile_image'],
    #                             mobile_no=request.POST['mobile_no'])
    # personnelinfo = personnel_info(gender=request.POST['gender'],
    #                                father_name=request.POST['father_name'],
    #                                pan=request.POST['pan'],
    #                                dob=request.POST['dob'],
    #                                doj=request.POST['doj'],
    #                                contact=request.POST['contact'],
    #                                altr_email=request.POST['altr_email'],
    #                                blood_grp=request.POST['blood_grp'],
    #                                emp_id=request.POST['username'])

    # education = len(request.POST.getlist('passing_year'))
    # for i in range(0, education):
    #     educational_info.objects.create(
    #         passing_year=request.POST.getlist('passing_year')[i],
    #         marks=request.POST.getlist('marks')[i],
    #         board=request.POST.getlist('board')[i],
    #         subject=request.POST.getlist('subject')[i],
    #         university=request.POST.getlist('university')[i],
    #         branch=request.POST.getlist('branch')[i],
    #         level=request.POST.getlist('level')[i],
    #         emp_id=request.POST['username']
    #     )

    # experience = experience_info(organization=request.POST['organization'],
    #                              designation=request.POST['designation'],
    #                              period_from=request.POST['period_from'],
    #                              period_to=request.POST['period_to'],
    #                              leaving_reason=request.POST['leaving_reason'],
    #                              emp_id=request.POST['username'])
    user.save()
    # personnelinfo.save()
    # addemp.save()
    # education.save()
    # experience.save()
    # return HttpResponse(request.POST.getlist('passing_year'))
    return render(request, 'hr/index.html')

def profile(request):
    return render(request, 'hr/profile.html')

def editprofile(request):
    return render(request, 'hr/editprofile.html')

def setting(request):
    return render(request, 'hr/setting.html')

def changepwd(request):
    return render(request, 'hr/changepwd.html')

def login(request):
    return render(request, 'hr/login.html')

def register(request):
    return render(request, 'hr/register.html')

def forgot_pw(request):
    return render(request, 'hr/forgot-password.html')

