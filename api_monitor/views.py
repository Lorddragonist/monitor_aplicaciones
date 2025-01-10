from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import ApiEndpoint
from .forms import ApiEndpointForm

@login_required
def api_list(request):
    apis = ApiEndpoint.objects.all()  # Mostrar todas las APIs sin filtrar por usuario
    return render(request, 'api_monitor/api_list.html', {'apis': apis})

@login_required
def api_create(request):
    if request.method == 'POST':
        form = ApiEndpointForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el formulario directamente sin asignar usuario
            return redirect('api_list')
    else:
        form = ApiEndpointForm()
    return render(request, 'api_monitor/api_form.html', {'form': form})

@login_required
def api_update(request, pk):
    api = get_object_or_404(ApiEndpoint, pk=pk)  # Eliminar referencia a 'user'
    if request.method == 'POST':
        form = ApiEndpointForm(request.POST, instance=api)
        if form.is_valid():
            form.save()
            return redirect('api_list')
    else:
        form = ApiEndpointForm(instance=api)
    return render(request, 'api_monitor/api_form.html', {'form': form})

@login_required
def api_delete(request, pk):
    api = get_object_or_404(ApiEndpoint, pk=pk)  # Eliminar referencia a 'user'
    if request.method == 'POST':
        api.delete()
        return redirect('api_list')
    return render(request, 'api_monitor/api_confirm_delete.html', {'api': api})

