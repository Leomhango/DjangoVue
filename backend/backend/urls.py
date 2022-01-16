from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_auth', include(
        'rest_framework.urls', namespace='rest_framework')),
    path('', include('main.urls'))
]
