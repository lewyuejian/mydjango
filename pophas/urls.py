#!/usr/bin/env python3
# encoding: utf-8
'''
@author: lewyuejian
@license: (C) Copyright 2017-2019, Personal exclusive right.
@contact: lewyuejian@163.com
@software: tool
@application:
@file: urls.py
@time: 2019/9/25 10:08
@desc:
'''
from django.urls import path
from pophas.views import Login
from django.contrib import admin

app_name = 'pophas'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.login),
    path('index/', Login.index),

]
