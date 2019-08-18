from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'backend_app'

urlpatterns = [
    path('', views.BackendIndex.as_view(), name='index'),
    path('app_list/', views.ApplicationsView.as_view(), name='app_list'),
    path('app_edit/<int:pk>', views.ApplicationEditView.as_view(), name='app_edit'),
]
