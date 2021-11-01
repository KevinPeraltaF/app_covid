from django.contrib import admin

from .models import ModeloBase,Menu,MenuGrupo,Permission
# Register your models here.





@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    '''Admin View for Menu'''

    list_display = ('titulo','descripcion','icono','url','es_modulo_principal','activo','principal','usuario_creacion','fecha_creacion','usuario_modificacion','fecha_modificacion',)
    list_filter = ('titulo','descripcion','es_modulo_principal','activo','principal',)
    search_fields = ('titulo','descripcion',)