#Django
from django.urls import path
from covid import views as key

urlpatterns = [
 #MENU
    path('', key.Dashboard_view.as_view(), name="dashboard" ),
    path('menu/', key.MenuListView.as_view(), name="menu_listar") ,
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

    path('usuario/Detalle/<int:pk>', key.UsuarioDetailView.as_view(), name="usuario_detalle") ,

 

]