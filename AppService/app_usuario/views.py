from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, RolForm, SolicitudForm
from .models import Usuario, Rol, SolicitudServicio
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.dateparse import parse_date

def index(request):
    usuarios = Usuario.objects.all()
    return render(request, 'app_usuario/user.html', {'usuarios': usuarios})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('app_usuario:index')
    else:
        form = UserForm()
        context = {'form':form}
        return render(request, 'app_usuario/create_user.html', context)
    
def update_user(request, id):
    user = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('app_usuario:index')
    else:
        form = UserForm(instance=user)
        context = {'form':form}
        return render(request, 'app_usuario/update_user.html', context)
    
def delete_user(request, id):
    try:
        user = get_object_or_404(Usuario, id=id)
        user.delete()
        return JsonResponse({'status': 'success'}, status=200)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
@csrf_exempt
def toggle_user_status(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        try:
            usuario = Usuario.objects.get(id=user_id)
            usuario.activo = not usuario.activo  # Cambia el estado
            usuario.save()
            return JsonResponse({"success": True, "new_status": usuario.activo})
        except Usuario.DoesNotExist:
            return JsonResponse({"success": False, "error": "Usuario no encontrado"})
    return JsonResponse({"success": False, "error": "Método no permitido"})

def index_rol(request):
    roles = Rol.objects.all()
    return render(request, 'app_usuario/rol.html', {'roles': roles})

def create_rol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('app_usuario:index_rol')
    else:
        form = RolForm()
        context = {'form':form}
        return render(request, 'app_usuario/create_rol.html', context)

def delete_rol(request, id):
    try:
        rol = get_object_or_404(Rol, id=id)
        rol.delete()
        return JsonResponse({'status': 'success'}, status=200)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
def index_solicitud(request):
    # Obtener los parámetros de búsqueda
    query_nombre = request.GET.get('q', '')
    query_fecha = request.GET.get('fecha', '')
    
    # Filtrar solicitudes
    solicitudes = SolicitudServicio.objects.all()
    
    # Filtrar por nombre/descripción si hay un término de búsqueda
    if query_nombre:
        solicitudes = solicitudes.filter(
            Q(nombre__icontains=query_nombre) | 
            Q(descripcion__icontains=query_nombre)
        )
    
    # Filtrar por fecha si se proporciona una fecha
    if query_fecha:
        try:
            fecha_filtro = parse_date(query_fecha)
            if fecha_filtro:
                solicitudes = solicitudes.filter(fecha_solicitud=fecha_filtro)
        except ValueError:
            # Manejar cualquier error de parsing de fecha
            pass
    
    # Paginación
    paginator = Paginator(solicitudes, 10)  # 10 solicitudes por página
    page = request.GET.get('page')
    
    try:
        solicitudes = paginator.page(page)
    except PageNotAnInteger:
        solicitudes = paginator.page(1)
    except EmptyPage:
        solicitudes = paginator.page(paginator.num_pages)
    
    return render(request, 'app_usuario/solicitud_servicio.html', {
        'solicitudes': solicitudes,
        'query_nombre': query_nombre,
        'query_fecha': query_fecha
    })

def create_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)  
            solicitud.usuario = form.cleaned_data['usuario']
            solicitud.save()
        return redirect('app_usuario:index_solicitud')
    else:
        form = SolicitudForm()
        context = {'form': form}
        return render(request, 'app_usuario/create_solicitud.html', context)
    
def delete_solicitud(request, id):
    try:
        solicitud = get_object_or_404(SolicitudServicio, id=id)
        solicitud.delete()
        return JsonResponse({'status': 'success'}, status=200)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
def update_solicitud(request, id):
    solicitud = get_object_or_404(SolicitudServicio, id=id)
    if request.method == 'POST':
        form = SolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            return redirect('app_usuario:index_solicitud')
    else:
        form = SolicitudForm(instance=solicitud)
    
    context = {'form':form}
    return render(request, 'app_usuario/update_solicitud.html', context)