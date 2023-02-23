from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.forms import modelform_factory

from webapp.forms import viajeForm

from webapp.models import Viajess

from django.db.models import Sum #debes importar este metodo


# Create your views here.






def bienvenido(request):
    #Diccionarios principales
    total_registros = Viajess.objects.count()
    viajes_var = Viajess.objects.all()
    no_viajes_var = {'no_viajes':total_registros, 'no_viajes_lista':viajes_var}

    #Total de Ganancias

    total_precios = Viajess.objects.aggregate(Sum('precio_viaje'))['precio_viaje__sum'] or 0
    ganancias_var = {'ganancias':total_precios}

    return render(request, 'index.html', {**no_viajes_var, **ganancias_var})


def detalleViaje(request, id):
    #viajes_var = Viajess.objects.get(pk=id) #Creacion de la variable con los datos que traera el diccionario
    #viajes_dic_var = {'detalles:':viajes_detalles_var} #Diccionario en una variable
    viajes_var = get_object_or_404(Viajess, pk=id)


    return render(request, 'opciones/detalles.html', {'viajes':viajes_var})
from django.http import HttpResponse


#viajeForm = modelform_factory(Viajess, exclude=[])

def agregarViaje(request):
    # Verifica si la solicitud es mediante el método POST
    if request.method == 'POST':
        # Si es así, crea una instancia de viajeForm con los datos recibidos en la solicitud
        formViaje = viajeForm(request.POST)
        # Verifica si los datos ingresados son válidos según las reglas definidas en la clase viajeForm
        if formViaje.is_valid():
            # Si son válidos, guarda los datos ingresados en la base de datos
            formViaje.save()
            # Redirige al usuario a la página principal ('index')
            return redirect('index')
    # Si la solicitud no es mediante POST, crea una instancia de viajeForm vacía
    else:
        formViaje = viajeForm()
    # Renderiza la plantilla 'opciones/agregar.html' con el formulario 'formViaje' como contexto
    return render(request, 'opciones/agregar.html', {'FormViaje': formViaje})



def editarViaje(request, id):
    viajes_id = get_object_or_404(Viajess, pk=id)
    if request.method == 'POST':
        formViaje = viajeForm(request.POST, instance=viajes_id)
        if formViaje.is_valid():
            formViaje.save()
            return redirect('index')
    else:
        formViaje = viajeForm(instance=viajes_id)
    return render(request, 'opciones/editar.html', {'FormViaje': formViaje})



def eliminarViaje(request, id):
    viajes_id = get_object_or_404(Viajess, pk=id)
    if viajes_id:
        viajes_id.delete()
    return redirect('index')

def eliminarViaje_all(request):
    Viajess.objects.all().delete()
    return redirect('index')


