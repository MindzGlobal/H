from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home_teamlead),
    url(r'^index_teamlead$', views.index_teamlead, name='index_teamlead'),
    url(r'^holidays_teamlead$', views.holidays_teamlead, name='holidays_teamlead'),
    url(r'^attendance_teamlead$', views.attendance_teamlead, name='attendance_teamlead'),
    url(r'^salary_teamlead$', views.salary_teamlead, name='salary_teamlead'),
    url(r'^salaryview_teamlead$', views.salaryview_teamlead, name='salaryview_teamlead'),
    url(r'^profile_teamlead$', views.profile_teamlead, name='profile_teamlead'),
    url(r'^editprofile_teamlead$', views.editprofile_teamlead, name='editprofile_teamlead'),
    url(r'^compose_teamlead$', views.compose_teamlead, name='compose_teamlead'),
    url(r'^changepwd_teamlead$', views.changepwd_teamlead, name='changepwd_teamlead'),
    url(r'^leavesRequest_teamlead$', views.leave_teamlead, name='leave_teamlead'),
    url(r'^mailview_teamlead$', views.mailview_teamlead, name='mailview_teamlead'),
    url(r'^employee_teamlead$', views.employee_teamlead, name='employee_teamlead'),
]
