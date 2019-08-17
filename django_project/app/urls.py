from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_application', views.new_application, name='new_application'),
    path('campagin_status', views.campagin_status, name='new_application'),
]
