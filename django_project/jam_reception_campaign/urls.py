from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login

urlpatterns = [
    path('', include('app.urls', namespace='app')),
    path('login/', LoginView.as_view(
        template_name='backend_app/login.html'
    ), name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('back/', include('backend_app.urls', namespace='backend_app')),
    path('admin/', admin.site.urls),
]
