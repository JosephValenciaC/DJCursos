from django.db import models
from ckeditor.fields import RichTextField



class Cursos(models.Model): #Define la estructura de la tabla
    
    NombreCurso = models.CharField(max_length=100, verbose_name="Curso") #Define el tipo de dato y el tamaño
    NombreTutor = models.CharField(max_length=150, verbose_name="Tutor")
    Descripcion = models.TextField() 
    Link = models.CharField(max_length=150, verbose_name="Enlace del Curso")
    Platafroma = models.CharField(max_length=50, verbose_name="Plataforma")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Imagen del Curso")
    created = models.DateTimeField(auto_now_add=True) #Fecha de creacion
    update = models.DateTimeField(auto_now_add=True) #Fecha de actualizacion
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["created"]
    def __str__(self):
        return self.NombreCurso 
    
    

class Actividad(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave de Actividad")
    nombreCurso = models.ForeignKey(Cursos, on_delete=models.CASCADE, verbose_name="Curso")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    descripCurso = RichTextField(verbose_name="Descripcion del Curso")
    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        ordering = ["-created"]
        
        def __str__(self):
            return self.nombreCurso