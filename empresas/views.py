from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Empresa
from users.models import User
from django.core.files.storage import FileSystemStorage
from .models import Empresa, Documento

@login_required
def empresas_contador(request):
    empresas = Empresa.objects.filter(contador=request.user)
    return render(request, "empresas/lista_empresas.html", {"empresas": empresas})

@login_required
def empresa_cliente(request):
    empresa = Empresa.objects.filter(cliente=request.user).first()
    return render(request, "empresas/mi_empresa.html", {"empresa": empresa})

@login_required
def subir_documento(request):
    if request.user.role != "cliente":
        return redirect("/")

    empresa = Empresa.objects.filter(cliente=request.user).first()

    if request.method == "POST" and request.FILES.get("archivo"):
        Documento.objects.create(
            empresa=empresa,
            archivo=request.FILES["archivo"]
        )
        return redirect("mis_documentos")

    return render(request, "empresas/subir_documento.html")

@login_required
def mis_documentos(request):
    empresa = Empresa.objects.filter(cliente=request.user).first()
    docs = Documento.objects.filter(empresa=empresa).order_by("-fecha_subida")
    return render(request, "empresas/mis_documentos.html", {"docs": docs})


@login_required
def documentos_contador(request):
    if request.user.role != "contador":
        return redirect("/")

    # documentos de las empresas del contador
    docs = Documento.objects.filter(empresa__contador=request.user).order_by("-fecha_subida")
    return render(request, "empresas/documentos_contador.html", {"docs": docs})


@login_required
def revisar_documento(request, id):
    if request.user.role != "contador":
        return redirect("/")

    doc = Documento.objects.get(id=id)

    if request.method == "POST":
        estado = request.POST.get("estado")
        comentarios = request.POST.get("comentarios")

        doc.estado = estado
        doc.comentarios = comentarios
        doc.save()

        return redirect("documentos_contador")

    return render(request, "empresas/revisar_documento.html", {"doc": doc})
