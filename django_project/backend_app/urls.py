from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'backend_app'

urlpatterns = [
    path('', views.BackendIndex.as_view(), name='index'),
]
