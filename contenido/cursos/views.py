from django.shortcuts import render
from .models import Cursos

def registros(request):
    cursos=Cursos.objects.all()
    return render(request, "registros/cursos.html", {"cursos":cursos})