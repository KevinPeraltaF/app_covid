#Django
from django.urls import path
from covid import views as key

urlpatterns = [
 #MENU
    path('', key.Dashboard_view.as_view(), name="dashboard" ),
    path('menu/', key.MenuListView.as_view(), name="menu_listar") ,
    path('menu/acceso/', key.Menu_AccesoListView.as_view(), name="menuAcceso_listar") ,
    path('menu/acceso/editar/<int:pk>', key.Menu_AccesoUpdateView.as_view(), name="menuAcceso_editar") ,
    path('menu/crear/', key.MenuCreateView.as_view(), name="menu_crear") ,
    path('menu/editar/<int:pk>', key.MenuUpdateView.as_view(), name="menu_editar") ,
    path('menu/Eliminar/<int:pk>', key.MenuDeleteView.as_view(), name="menu_eliminar") ,
    path('menu/Detalle/<int:pk>', key.MenuDetailView.as_view(), name="menu_detalle") ,

    path('grupo/', key.GrupoListView.as_view(), name="grupo_listar") ,
    path('grupo/crear/', key.GrupoCreateView.as_view(), name="grupo_crear") ,
    path('grupo/editar/<int:pk>', key.GrupoUpdateView.as_view(), name="grupo_editar") ,
    path('grupo/Eliminar/<int:pk>', key.GrupoDeleteView.as_view(), name="grupo_eliminar") ,
    path('grupo/Detalle/<int:pk>', key.GrupoDetailView.as_view(), name="grupo_detalle") ,


    path('usuario/', key.UsuarioListView.as_view(), name="usuario_listar") ,
    path('usuario/crear/', key.UsuarioCreateView.as_view(), name="usuario_crear") ,
    path('usuario/editar/<int:pk>', key.UsuarioUpdateView.as_view(), name="usuario_editar") ,
    path('usuario/Eliminar/<int:pk>', key.UsuarioDeleteView.as_view(), name="usuario_eliminar") ,
    path('usuario/Detalle/<int:pk>', key.UsuarioDetailView.as_view(), name="usuario_detalle") ,


    path('MyPerfil/', key.PerfilUpdateView.as_view(), name="perfilUsuario") ,
    path('MyPerfil/change-password/', key.PasswordChangeView.as_view(),name="CambiarContraseña" ),
    
    
    path('especialidad/', key.EspecialidadMedicoListView.as_view(), name="especialidadMedico_listar") ,
    path('especialidad/crear/', key.EspecialidadMedicoCreateView.as_view(), name="especialidadMedico_crear") ,
    path('especialidad/editar/<int:pk>', key.EspecialidadMedicoUpdateView.as_view(), name="especialidadMedico_editar") ,
    path('especialidad/Eliminar/<int:pk>', key.EspecialidadMedicoDeleteView.as_view(), name="especialidadMedico_eliminar") ,
    path('especialidad/Detalle/<int:pk>', key.EspecialidadMedicoDetailView.as_view(), name="especialidadMedico_detalle") ,
  
  
    path('medico/', key.MedicoListView.as_view(), name="medico_listar") ,
    path('medico/crear/', key.MedicoCreateView.as_view(), name="medico_crear") ,
    path('medico/editar/<int:pk>', key.MedicoUpdateView.as_view(), name="medico_editar") ,
    path('medico/Eliminar/<int:pk>', key.MedicoDeleteView.as_view(), name="medico_eliminar") ,
    path('medico/Detalle/<int:pk>', key.MedicoDetailView.as_view(), name="medico_detalle") ,
    
    path('paciente/', key.PacienteListView.as_view(), name="paciente_listar") ,
    path('paciente/crear/', key.PacienteCreateView.as_view(), name="paciente_crear") ,
    path('paciente/editar/<int:pk>', key.PacienteUpdateView.as_view(), name="paciente_editar") ,
    path('paciente/Eliminar/<int:pk>', key.PacienteDeleteView.as_view(), name="paciente_eliminar") ,
    path('paciente/Detalle/<int:pk>', key.PacienteDetailView.as_view(), name="paciente_detalle") ,
    
    
    path('report/', key.ReportView.as_view(),name='reporte'),
    
    
    path('rayx/',key.RayxListView.as_view(),name="rayx_listar"),
    path('rayx/crear/',key.RayxCreateView.as_view(),name="rayx_crear"),
    path('rayx/editar/<int:pk>',key.RayxUpdateView.as_view(),name="rayx_editar"),
    path('rayx/Eliminar/<int:pk>',key.RayxDeleteView.as_view(),name="rayx_eliminar"),
    path('rayx/Detalle/<int:pk>',key.RayxDetailView.as_view(),name="rayx_detalle"),
    path('rayx/DetallePac/<int:pk>',key.RayxPacDetailView.as_view(),name="rayx_detalle_paciente"),
    
    path('myresultado/',key.MyresultListView.as_view(),name="myresultado_listar"),
    path('myresultado/Detalle/<int:pk>',key.MyresultRayxDetailView.as_view(),name="myresultado_detalle"), 
     
    path('vacuna/', key.VacunaListView.as_view(), name="vacuna_listar") ,
    path('vacuna/crear/', key.VacunaCreateView.as_view(), name="vacuna_crear") ,
    path('vacuna/editar/<int:pk>', key.VacunaUpdateView.as_view(), name="vacuna_editar") ,
    path('vacuna/Eliminar/<int:pk>', key.VacunaDeleteView.as_view(), name="vacuna_eliminar") ,
    path('vacuna/Detalle/<int:pk>', key.VacunaDetailView.as_view(), name="vacuna_detalle") ,
  
  
]