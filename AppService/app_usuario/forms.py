from django import forms
from app_usuario.models import Usuario, Rol, SolicitudServicio

class UserForm(forms.ModelForm):
    rol = forms.ModelChoiceField(
        queryset=Rol.objects.all(),
        empty_label="Seleccione un rol",
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Rol",
    )
    class Meta:
        model = Usuario
        fields = [ 'nombre', 'apellido', 'email', 'telefono', 'direccion', 'empresa', 'rol']

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = [ 'nombre', 'acceso' ]

class SolicitudForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        empty_label="Seleccione un usuario",
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Usuario",
    )
    fecha_solicitud = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'format': '%Y-%m-%d'}),
        label="Fecha de solicitud",
    )
    class Meta:
        model = SolicitudServicio
        fields = [ 'usuario', 'nombre', 'descripcion', 'fecha_solicitud']
