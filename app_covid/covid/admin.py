from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ModeloBase,Menu,Permission, User, EspecialidadMedico,Medico,Paciente,Analisis_Radiografico,Vacuna
# Register your models here.
admin.site.register(User, UserAdmin)

admin.site.register(Analisis_Radiografico)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    '''Admin View for Menu'''

    list_display = ('titulo','descripcion','icono','url','activo','usuario_creacion','fecha_creacion','usuario_modificacion','fecha_modificacion',)
    list_filter = ('titulo','descripcion','activo',)
    search_fields = ('titulo','descripcion',)
    
    
@admin.register(EspecialidadMedico)
class EspecialidadMedicoAdmin(admin.ModelAdmin):
    '''Admin View for EspecialidadMedico'''

    list_display = ('descripcion','usuario_creacion','fecha_creacion','usuario_modificacion','fecha_modificacion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)
    
@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    '''Admin View for Medico'''

    list_display = ('usuario','especialidad','usuario_creacion','fecha_creacion','usuario_modificacion','fecha_modificacion',)
    list_filter = ('usuario','especialidad',)
    search_fields = ('usuario',)
    

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    '''Admin View for Paciente'''

    list_display = ('usuario','direccion','usuario_creacion','fecha_creacion','usuario_modificacion','fecha_modificacion','fec_nac',)
    list_filter = ('usuario','direccion',)
    search_fields = ('usuario',)
    


@admin.register(Vacuna)
class VacunaAdmin(admin.ModelAdmin):
    '''Admin View for Vacuna'''

    list_display = ('descripcion','usuario_creacion','fecha_creacion','usuario_modificacion','fecha_modificacion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)