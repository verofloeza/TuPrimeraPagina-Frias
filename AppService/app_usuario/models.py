from django.db import models

class Usuario (models.Model):
    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre",
        help_text="Introduce el nombre del usuario."
    )
    apellido = models.CharField(
        max_length=100,
        verbose_name="Apellido",
        help_text="Introduce el apellido del usuario.",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Correo Electrónico",
        help_text="Introduce un correo electrónico válido.",
    )
    telefono = models.IntegerField(
        verbose_name="Teléfono",
        help_text="Introduce un número de teléfono válido.",
        null=True,
        blank=True,
    )
    empresa = models.CharField(
        max_length=100,
        verbose_name="Empresa",
        help_text="Nombre de la empresa.",
        null=True,
        blank=True,
    )
    direccion = models.CharField(
        max_length=100,
        verbose_name="Dirección",
        help_text="Introduce la dirección del usuario.",
        null=True,
        blank=True,
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Indica si el usuario está activo."
    )
    rol = models.ForeignKey(
        'Rol',
        on_delete=models.CASCADE,
        related_name='usuarios',
        verbose_name="Rol",
        help_text="Rol asignado al usuario.",
        default=1 
    )

    def __str__(self):
        return f'{self.apellido}, {self.nombre} - Empresa: {self.empresa} '

class Rol(models.Model):
    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre",
        help_text="Introduce el nombre del usuario."
    )
    acceso = models.IntegerField(
        verbose_name="Acceso",
        help_text="Introduce el nivel de acceso del usuario.",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.nombre}'
    
class SolicitudServicio(models.Model):
    usuario = models.ForeignKey(
        Usuario,  
        on_delete=models.CASCADE,
        verbose_name="Usuario",
        help_text="Introduce el usuario asignado.",
        null=True,
        blank=True,
    )
    fecha_solicitud = models.DateField()
    nombre = models.CharField(
        max_length=100,
        verbose_name="Título de la solicitud",
        help_text="Introduce que solicita.",
        null=True,
        blank=True,
    )
    descripcion = models.CharField(
        max_length=300,
        verbose_name="Descripcion",
        help_text="Introduce lo que busca.",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Título: {self.nombre}: Descripción: {self.descripcion}'

