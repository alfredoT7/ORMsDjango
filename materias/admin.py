from django.contrib import admin
from .models import Carrera,Entrega,Facultad,TipoArchivo,Tarea,Materia
# Register your models here.
admin.site.register(Carrera)
admin.site.register(Entrega)
admin.site.register(Facultad)
admin.site.register(TipoArchivo)
admin.site.register(Tarea)
admin.site.register(Materia)