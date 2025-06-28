from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("admin_tools.urls") ),
    path('site-admin/', admin.site.urls),
]
