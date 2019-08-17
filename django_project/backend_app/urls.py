from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.BackendIndex.as_view(), name='index'),
]
