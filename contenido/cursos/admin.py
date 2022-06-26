from typing import Sequence
from django.contrib import admin
from .models import Cursos


class AdministartModelo(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'update')
    

    
admin.site.register(Cursos, AdministartModelo)


