from django.urls import path
from .views import empresas_contador, empresa_cliente
from .views import subir_documento, mis_documentos
from .views import documentos_contador, revisar_documento

urlpatterns = [
    path("contador/empresas/", empresas_contador, name="empresas_contador"),
    path("cliente/empresa/", empresa_cliente, name="empresa_cliente"),
    path("cliente/documentos/", mis_documentos, name="mis_documentos"),
    path("cliente/subir/", subir_documento, name="subir_documento"),
    path("contador/documentos/", documentos_contador, name="documentos_contador"),
    path("contador/documentos/revisar/<int:id>/", revisar_documento, name="revisar_documento"),
]
