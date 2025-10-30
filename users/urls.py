from django.urls import path
from .views import login_view, logout_view, register_view
from .views import dashboard_contador, dashboard_cliente

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("contador/", dashboard_contador, name="dashboard_contador"),
    path("cliente/", dashboard_cliente, name="dashboard_cliente"),
]
