from django.contrib import admin

# Register your models here.

from .models import Laboratorio,Registro

admin.site.register(Laboratorio)
admin.site.register(Registro)
