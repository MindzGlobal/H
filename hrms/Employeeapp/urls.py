from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home_employee),
    url(r'^index_employee$', views.index_employee, name='index_employee'),
    url(r'^holidays_employee$', views.holidays_employee, name='holidays_employee'),
    url(r'^attendance_employee$', views.attendance_employee, name='attendance_employee'),
    url(r'^salary_employee$', views.salary_employee, name='salary_employee'),
    url(r'^salaryview_employee$', views.salaryview_employee, name='salaryview_employee'),
    url(r'^profile_employee', views.profile_employee, name='profile_employee'),
    url(r'^editprofile_employee', views.editprofile_employee, name='editprofile_employee'),
    url(r'^compose$', views.compose, name='compose_employee'),
    url(r'^changepwd_employee', views.changepwd_employee, name='changepwd_employee'),
    url(r'^leavesRequest_employee$', views.leave_employee, name='leave_employee'),
    url(r'^mailview_employee$', views.mailview_employee, name='mailview_employee'),

]