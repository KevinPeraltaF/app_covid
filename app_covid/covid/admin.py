from django.contrib import admin

from .models import ModeloBase,Menu,Permission, User, EspecialidadMedico,Medico,Paciente
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''Admin View for Menu'''

    list_display = ('username','first_name','last_name','email','is_active','is_staff','is_superuser',)
    list_filter = ('username','first_name','last_name','email','is_staff','is_active',)
    search_fields = ('username','first_name','last_name','email',)


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

    list_display = ('usuario','direccion','usuario_creacion','fecha_creacion','usuario_modificacion','fecha_modificacion',)
    list_filter = ('usuario','direccion',)
    search_fields = ('usuario',)