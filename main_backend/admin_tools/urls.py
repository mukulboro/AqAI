from django.urls import path
from . import views

urlpatterns = [
   path("login/", views.admin_login, name="admin_login"),
   path("dashboard/", views.dasboard_start, name="first_dash")
]