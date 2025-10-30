from django.db import models
from users.models import User

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    nit = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    cliente = models.OneToOneField(User, on_delete=models.CASCADE, related_name="empresa_cliente")
    contador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="empresas_contador")

    def __str__(self):
        return self.nombre

class Documento(models.Model):
    ESTADOS = (
        ("pendiente", "Pendiente"),
        ("aprobado", "Aprobado"),
        ("rechazado", "Rechazado"),
    )

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="documentos")
    archivo = models.FileField(upload_to="documentos/")
    fecha_subida = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.empresa.nombre} - {self.archivo.name}"

