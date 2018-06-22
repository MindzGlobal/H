# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'admin/login.html')

def forgot_pwd(request):
    return render(request, 'admin/forgot-password.html')
