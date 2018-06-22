from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home),
    url(r'^index_manager$', views.index_manager, name='index_manager'),
    url(r'^Holidays_manager$', views.holidays_manager, name='holidays_manager'),
    url(r'^Employees_manager$', views.employees_manager, name='employees_manager'),
    url(r'^Attendance_manager$', views.attendance_manager, name='attendance_manager'),
    url(r'^Designations_manager', views.designations_manager, name='designations_manager'),
    url(r'^Leaves_manager$', views.leaves_manager, name='leaves_manager'),
    url(r'^Leads_manager$', views.leads_manager, name='leads_manager'),
    url(r'^Salary_manager$', views.salary_manager, name='salary_manager'),
    url(r'^Salary_manager_emp$', views.salary_manager_emp, name='salary_manager_emp'),
    url(r'^Salaryview_manager$', views.salaryview_manager, name='salaryview_manager'),
    url(r'^Sndmsg_manager$', views.sndmsg_manager, name='sndmsg_manager'),
    url(r'^Mailview', views.mailview, name='mailview'),
    url(r'^Profile_manager', views.profile_manager, name='profile_manager'),
    url(r'^Editprofile_manager', views.editprofile_manager, name='editprofile_manager'),
    url(r'^Changepwd_manager', views.changepwd_manager, name='changepwd_manager'),
    url(r'^Login',views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^forgot_pw', views.forgot_pw, name='forgot_pw'),


    url(r'^Login',views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^forgot_pw', views.forgot_pw, name='forgot_pw'),

]