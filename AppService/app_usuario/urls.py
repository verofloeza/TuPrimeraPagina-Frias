from django.urls import path
from . import views

app_name = 'app_usuario'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user/', views.create_user, name='create_user'),
    path('update_user/<int:id>/', views.update_user, name='update_user'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    path("toggle_user_status/", views.toggle_user_status, name="toggle_user_status"),
    path('rol/', views.index_rol, name='index_rol'),
    path('create_rol/', views.create_rol, name='create_rol'),
    path('roles/delete/<int:id>/', views.delete_rol, name='delete_rol'),
    path('solicitudes/', views.index_solicitud, name='index_solicitud'),
    path('create_solicitud/', views.create_solicitud, name='create_solicitud'),
    path('update_solicitud/<int:id>/', views.update_solicitud, name='update_solicitud'),
    path('solicitudes/delete/<int:id>/', views.delete_solicitud, name='delete_solicitud'),
]