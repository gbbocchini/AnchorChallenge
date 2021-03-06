from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import Register

app_name = "accounts"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register", Register.as_view(), name="register"),
]
