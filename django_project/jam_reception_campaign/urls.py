from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls', namespace='app')),
    path('back/', include('backend_app.urls', namespace='backend_app')),
    path('admin/', admin.site.urls),
]
