from django.shortcuts import render
from .models import DatosPersonales

def cv_view(request):
    perfil = DatosPersonales.objects.get(idperfil=123)

    context = {
        'perfil': perfil,
        'experiencias': perfil.experiencias.filter(activarparaqueseveaenfront=True),
        'cursos': perfil.cursos.filter(activarparaqueseveaenfront=True),
    }

    return render(request, 'mi_web/index.html', context)
