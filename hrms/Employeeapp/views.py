from django.shortcuts import render

# Create your views here.

def home_employee(request):
    return render(request, 'employee/base_employee.html')

def index_employee(request):
    return render(request, 'employee/index_employee.html')

def holidays_employee(request):
    return render(request, 'employee/holidays_employee.html')

def attendance_employee(request):
    return render(request, 'employee/attendance_employee.html')

def salary_employee(request):
    return render(request, 'employee/salary_employee.html')

def salaryview_employee(request):
    return render(request, 'employee/salaryview_employee.html')

def profile_employee(request):
    return render(request, 'employee/profile_employee.html')

def editprofile_employee(request):
    return render(request, 'employee/editprofile_employee.html')

def changepwd_employee(request):
    return render(request, 'employee/changepwd_employee.html')

def leave_employee(request):
    return render(request, 'employee/leave_employee.html')

def compose(request):
    return render(request, 'employee/compose_employee.html')

def mailview_employee(request):
    return render(request, 'employee/mailview_employee.html')