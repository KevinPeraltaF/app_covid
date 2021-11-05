#DJANGO
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import (CreateView, UpdateView, DeleteView,FormView)
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordChangeView
#MODELS
from .models import Menu, Group, User,Menu_Groups
#FORMS
from .forms import  MenuForm,GrupoForm, UserForm,MenuGrupoForm,PerfilForm,CambiarContraseñaForm
#auditoria - crum django
from crum import get_current_user
#MY VIEWS
class Dashboard_view(LoginRequiredMixin,TemplateView):
    template_name = "registration/dashboard.html"
    def get_context_data(self, **kwargs):
        permisos = Group.objects.filter(user=self.request.user)
        context = super().get_context_data(**kwargs)
        context['titulo'] ="Menú Principal"
        if self.request.user.is_superuser:
            context['MenuSuperUser'] = Menu.objects.all()
        else:
            context['menu'] = Menu_Groups.objects.filter( group__in=permisos, activo =True, menu__activo = True)
        return context

#MENU
class MenuListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'covid.view_menu'
    paginate_by = 7
    model = Menu
    template_name = "menu/menu_listar.html"

    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")
        queryset = Menu.objects.all()
        if busqueda:
            queryset = Menu.objects.filter(
                Q(titulo__icontains= busqueda)|
                Q(descripcion__icontains= busqueda)
                ).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro  Menù de usuarios"
        return context

class MenuCreateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'covid.add_menu'
    model = Menu
    form_class = MenuForm
    template_name = "menu/menu_crear.html"
    success_url = reverse_lazy('menu_listar')
    success_message = 'Registro Guardado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Menù de usuarios"
        return context

class MenuDeleteView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'covid.delete_menu'
    model = Menu
    template_name = "menu/menu_eliminar.html"
    success_url = reverse_lazy('menu_listar')
    success_message = 'Registro Eliminado Exitosamente'
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MenuDeleteView, self).delete(request, *args, **kwargs)

class MenuUpdateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'covid.change_menu'
    model = Menu
    form_class = MenuForm
    template_name = "menu/menu_editar.html"
    success_url = reverse_lazy('menu_listar')
    success_message = 'Registro Editado Exitosamente'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro  Menù de usuarios"
        return context

class MenuDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'covid.view_menu'
    model = Menu
    template_name = "menu/menu_detalle.html"

#ACCESO A MODULOS DE ACUERDO AL GRUPO
class Menu_AccesoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'covid.view_menu_groups'
    paginate_by = 7
    model = Menu_Groups
    template_name = "menu/accesoModulo_listar.html"
    
    def get_queryset(self):
        busqueda = self.request.GET.get("grupo")
        queryset = Menu_Groups.objects.all()
        if busqueda:
            queryset = Menu_Groups.objects.filter(
                Q(group__id__icontains= busqueda)
                ).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = " Acceso a Módulo"
        context['grupos'] = Group.objects.all()
       
        return context

class Menu_AccesoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'covid.change_menu_groups'
    model = Menu_Groups
    form_class = MenuGrupoForm
    template_name = "menu/accesoModulo_editar.html"
    success_url = reverse_lazy('menuAcceso_listar')
    success_message = 'Registro Editado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Acceso a Módulo - Estado"
        return context

#GRUPOS
class GrupoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'auth.view_group'
    paginate_by = 7
    model = Group
    template_name = "grupo/grupo_listar.html"

    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")
        queryset = Group.objects.all()
        if busqueda:
            queryset = Group.objects.filter(
                Q(name__icontains= busqueda)
                ).distinct()
        return queryset
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro Grupos de usuarios"
        return context

class GrupoCreateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'auth.add_group'
    model = Group
    form_class = GrupoForm
    template_name = "grupo/grupo_crear.html"
    success_url = reverse_lazy('grupo_listar')
    success_message = 'Registro Guardado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Grupos de usuarios"
        return context

class GrupoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'auth.change_group'
    model = Group
    form_class = GrupoForm
    template_name = "grupo/grupo_editar.html"
    success_url = reverse_lazy('grupo_listar')
    success_message = 'Registro Editado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Grupos de usuarios"
        return context

class GrupoDeleteView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'auth.delete_group'
    model = Group
    template_name = "grupo/grupo_eliminar.html"
    success_url = reverse_lazy('grupo_listar')
    success_message = 'Registro Eliminado Exitosamente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(GrupoDeleteView, self).delete(request, *args, **kwargs)

class GrupoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'auth.view_group'
    model = Group
    template_name = "grupo/grupo_detalle.html"

#USUARIOS
class UsuarioListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'covid.view_user'
    paginate_by = 7
    model = User
    template_name = "usuario/usuario_listar.html"

    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")
        queryset = User.objects.all()
        if busqueda:
            queryset = User.objects.filter(
                Q(cedula__icontains= busqueda)|
                Q(email__icontains= busqueda)|
                Q(username__icontains= busqueda)|
                Q(first_name__icontains= busqueda)|
                Q(last_name__icontains= busqueda)
                ).distinct()
        return queryset


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de usuarios"
        return context

class UsuarioCreateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'covid.add_user'
    model = User
    form_class = UserForm
    template_name = "usuario/usuario_crear.html"
    success_url = reverse_lazy('usuario_listar')
    success_message = 'Registro Guardado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de usuarios"
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        #estableciendo password y usuario por defecto cedula
        form.instance.username = form.cleaned_data['cedula']
        form.instance.password = make_password(form.cleaned_data['cedula'])
        self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de usuarios"
        return context

class UsuarioUpdateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'covid.change_user'
    model = User
    form_class = UserForm
    template_name = "usuario/usuario_editar.html"
    success_url = reverse_lazy('usuario_listar')
    success_message = 'Registro Editado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de usuarios"
        return context

class UsuarioDeleteView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'covid.delete_user'
    model = User
    form_class = UserForm
    template_name = "usuario/usuario_eliminar.html"
    success_url = reverse_lazy('usuario_listar')
    success_message = 'Registro Eliminado Exitosamente'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(UsuarioDeleteView, self).delete(request, *args, **kwargs)

class UsuarioDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'covid.view_user'
    model = User
    template_name = "usuario/usuario_detalle.html"

#PERFIL DE USUARIO

class PerfilUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = User
    form_class = PerfilForm
    template_name = "usuario/perfilUsuario.html"
    success_url = reverse_lazy('perfilUsuario')
    success_message = 'Perfil Editado Exitosamente'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_object(self, queryset = None):
        return self.request.user

        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "My Perfil"
        return context
#cambiar contraseña
class PasswordChangeView(PasswordChangeView):
  template_name = 'usuario/cambiarContraseña.html'
  form_class = CambiarContraseñaForm
  success_url =reverse_lazy('logout')

  def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Cambiar Contraseña"
        return context