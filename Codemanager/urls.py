from django.contrib import admin
from django.urls import path, include, re_path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^jet/', include('jet.urls', 'jet')),
]
