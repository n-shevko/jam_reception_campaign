from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_application', views.new_application, name='new_application'),
    path('campagin_status', views.campagin_status, name='campagin_status'),
    path('save_application', views.save_application, name='save_application'),
    path('campagin_results', views.campagin_results, name='campagin_results'),
]
