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
  

]