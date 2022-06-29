
from typing import Optional, Sequence
from django.contrib import admin
from .models import Cursos


class AdministartModelo(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    list_display = ('NombreCurso', 'NombreTutor' ,'Descripcion', 'Platafroma')
    search_fields: Sequence[str] = ('NombreCurso', 'NombreTutor' ,'Descripcion', 'Platafroma')
    date_hierarchy: Optional[str] = 'created'
    list_filter = ('NombreTutor','Platafroma')
    

    
admin.site.register(Cursos, AdministartModelo)


