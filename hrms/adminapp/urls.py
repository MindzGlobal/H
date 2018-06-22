from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login , name='login'),
    url(r'^forgot_password$', views.forgot_pwd, name='forgot_pwd'),
]