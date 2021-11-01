#DJANGO
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
#MODELS
from .models import Menu, Group, User
#FORMS
from .forms import  MenuForm,GrupoForm

#MY VIEWS
class Dashboard_view(LoginRequiredMixin,TemplateView):
    template_name = "registration/dashboard.html"
    def get_context_data(self, **kwargs):
        permisos = Group.objects.filter(user=self.request.user)
        context = super().get_context_data(**kwargs)
        context['titulo'] ="Menú Principal"
        if self.request.user.is_superuser:
            context['menu'] = Menu.objects.filter(estado=True)
        else:
            context['menu'] = Menu.objects.filter(estado=True, activo = True, grupo__in=permisos)
        return context

#MENU
class MenuListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'covid.view_menu'
    model = Menu
    template_name = "menu/menu_listar.html"
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

#GRUPOS
class GrupoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'auth.view_group'
    model = Group
    template_name = "grupo/grupo_listar.html"

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
class UsuarioListView(LoginRequiredMixin,ListView):
    model = User
    template_name = "usuario/usuario_listar.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de usuarios"
        return context







