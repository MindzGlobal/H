from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home),
    url(r'^index$', views.index, name='index'),
    url(r'^Holidays$', views.holidays, name='holidays'),
    url(r'^Employees$', views.employees, name='employees'),
    url(r'^Attendance$', views.attendance, name='attendance'),
    url(r'^Departments$', views.departments, name='departments'),
    url(r'^Designations', views.designations, name='designations'),
    url(r'^Leaves$', views.leaves, name='leaves'),
    url(r'^Sndmsg_hr$', views.sndmsg_hr, name='sndmsg_hr'),
    url(r'^Viewmsg_hr$', views.viewmsg_hr, name='viewmsg_hr'),
    url(r'^Leads$', views.leads, name='leads'),
    url(r'^Salary$', views.salary, name='salary'),
    url(r'^Salaryview$', views.salaryview, name='salaryview'),
    url(r'^Addemployee$', views.addemployee, name='addemployee'),
    url(r'^addempdetail', views.addempdetail, name='addempdetail'),
    url(r'^Profile', views.profile, name='profile'),
    url(r'^Editprofile', views.editprofile, name='editprofile'),
    url(r'^Setting$', views.setting, name='setting'),
    url(r'^Salary_hr$', views.salary_hr, name='salary_hr'),
    url(r'^Salary_emp$', views.salary_emp, name='salary_emp'),
    url(r'^Changepwd$', views.changepwd, name='changepwd'),
    url(r'^Login$',views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^forgot_pw$', views.forgot_pw, name='forgot_pw'),
]