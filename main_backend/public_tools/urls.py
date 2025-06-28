from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("register/", views.RegisterManualView.as_view(), name="manual_registration"),
    path("register_google/", views.RegisterGoogleView.as_view(), name="google_registration"),
    path("login/", views.LoginManualView.as_view(), name="login_manual"),
    path("login_google/", views.LoginGoogleView.as_view(), name="login_google"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]