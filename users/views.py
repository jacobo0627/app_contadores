from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            if user.role == "contador":
                return redirect("dashboard_contador")
            else:
                return redirect("dashboard_cliente")
        else:
            messages.error(request, "Credenciales incorrectas")

    return render(request, "users/login.html")



def logout_view(request):
    logout(request)
    return redirect("login")


def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")  # cliente o contador

        User.objects.create_user(
            username=email,
            email=email,
            password=password,
            role=role
        )

        messages.success(request, "Cuenta creada, inicia sesión")
        return redirect("login")

    return render(request, "users/register.html")


@login_required
def dashboard_contador(request):
    return render(request, "users/dashboard_contador.html")

@login_required
def dashboard_cliente(request):
    return render(request, "users/dashboard_cliente.html")