#DJANGO
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.db.models.fields import DateField
from django.http.response import  HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordChangeView

#MODELS
from crum import get_current_user
from .models import Menu, Group, User,Menu_Groups, EspecialidadMedico,Vacuna,Medico,Paciente,Analisis_Radiografico
#FORMS
from .forms import  EspecialidadMedicoForm, MenuForm,GrupoForm, VacunaForm, UserForm,MenuGrupoForm,PerfilForm,CambiarContraseñaForm,MedicoForm,PacienteForm,RayxForm
#
from django.db.models import ProtectedError
#IA
from django.conf import settings
import os
""" import numpy as np
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import load_model """
#MY VIEWS
class Dashboard_view(LoginRequiredMixin,TemplateView):
    template_name = "registration/dashboard.html"
    def get_context_data(self, **kwargs):
        busqueda = self.request.GET.get("buscar")
        permisos = Group.objects.filter(user=self.request.user)
        context = super().get_context_data(**kwargs)
        context['titulo'] ="Menú Principal"
        if self.request.user.is_superuser:
            if not busqueda:
                context['MenuSuperUser'] = Menu.objects.all()
            else:
                context['MenuSuperUser'] = Menu.objects.filter(titulo__icontains=busqueda)
        else:
            if not busqueda:
                context['menu'] = Menu_Groups.objects.filter( group__in=permisos, activo =True, menu__activo = True)
            else:
                context['menu'] = Menu_Groups.objects.filter( group__in=permisos, activo =True, menu__activo = True,menu__titulo__icontains=busqueda)
        return context

class Error404View(TemplateView):
    template_name = 'error-404.html'

class Error500View(TemplateView):
    template_name = 'error-500.html'

    @classmethod
    def as_error_view(clase):
        objeto = clase.as_view()
        def view(request):
            result = objeto(request)
            result.render()
            return result
        return view

#MENU
class MenuListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'covid.view_menu'
    paginate_by = 7
    model = Menu
    template_name = "menu/menu_listar.html"

    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")
        queryset = Menu.objects.all().order_by("pk")
        if busqueda:
            queryset = Menu.objects.filter(
                Q(titulo__icontains= busqueda)|
                Q(descripcion__icontains= busqueda)
                ).distinct().order_by("pk")
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
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            error_messeage =  "Este registro no puede ser eliminado!!"
            messages.success(self.request,error_messeage)
            return HttpResponseRedirect(success_url)
     
        return HttpResponseRedirect(success_url)

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
        queryset = Menu_Groups.objects.all().order_by("pk")
        if busqueda:
            queryset = Menu_Groups.objects.filter(
                Q(group__id__icontains= busqueda)
                ).distinct().order_by("pk")
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
    model = Group
    paginate_by = 7
    template_name = "grupo/grupo_listar.html"

    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")
        queryset = Group.objects.all().order_by("pk")
        if busqueda:
            queryset = Group.objects.filter(
                Q(name__icontains= busqueda)
                ).distinct().order_by("pk")
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
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            error_messeage =  "Este registro no puede ser eliminado!!"
            messages.success(self.request,error_messeage)
            return HttpResponseRedirect(success_url)
     
        return HttpResponseRedirect(success_url)

class GrupoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'auth.view_group'
    model = Group
    template_name = "grupo/grupo_detalle.html"

#USUARIOS
class UsuarioListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'covid.view_user'
    model = User
    paginate_by = 7
    template_name = "usuario/usuario_listar.html"

    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")
        queryset = User.objects.all().order_by("pk")
        if busqueda:
            queryset = User.objects.filter(
                Q(cedula__icontains= busqueda)|
                Q(email__icontains= busqueda)|
                Q(username__icontains= busqueda)|
                Q(first_name__icontains= busqueda)|
                Q(last_name__icontains= busqueda)
                ).distinct().order_by("pk")
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
    template_name = "usuario/usuario_eliminar.html"
    success_url = reverse_lazy('usuario_listar')
    success_message = 'Registro Eliminado Exitosamente'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            error_messeage =  "Este registro no puede ser eliminado!!"
            messages.success(self.request,error_messeage)
            return HttpResponseRedirect(success_url)
     
        return HttpResponseRedirect(success_url)

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
    
#ESPECIALIDAD MEDICO
    
class EspecialidadMedicoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'covid.view_especialidadmedico'
    model = EspecialidadMedico
    paginate_by = 7
    template_name = "medico/especialidadMedico_listar.html"

    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")
        queryset = EspecialidadMedico.objects.all().order_by("pk")
        if busqueda:
            queryset = EspecialidadMedico.objects.filter(
                Q(descripcion__icontains= busqueda)
                ).distinct().order_by("pk")
        return queryset


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de especialidades de los Médicos"
        return context

class EspecialidadMedicoCreateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'covid.add_especialidadmedico'
    model = EspecialidadMedico
    form_class = EspecialidadMedicoForm
    template_name = "medico/especialidadMedico_crear.html"
    success_url = reverse_lazy('especialidadMedico_listar')
    success_message = 'Registro Guardado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Especialidades de los Médicos"
        return context

class EspecialidadMedicoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'covid.change_especialidadmedico'
    model = EspecialidadMedico
    form_class = EspecialidadMedicoForm
    template_name = "medico/especialidadMedico_editar.html"
    success_url = reverse_lazy('especialidadMedico_listar')
    success_message = 'Registro Editado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Especialidades de los Médicos"
        return context

class EspecialidadMedicoDeleteView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'covid.delete_especialidadmedico'
    model = EspecialidadMedico
    template_name = "medico/especialidadMedico_eliminar.html"
    success_url = reverse_lazy('especialidadMedico_listar')
    success_message = 'Registro Eliminado Exitosamente'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            error_messeage =  "Este registro no puede ser eliminado!!"
            messages.success(self.request,error_messeage)
            return HttpResponseRedirect(success_url)
     
        return HttpResponseRedirect(success_url)

class EspecialidadMedicoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'covid.view_especialidadmedico'
    model = EspecialidadMedico
    template_name = "medico/EspecialidadMedico_detalle.html"

#MEDICO
class MedicoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'covid.view_medico'
    model = Medico
    paginate_by = 7
    template_name = "medico/medico_listar.html"
    
    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")
        queryset = Medico.objects.all().order_by("pk")
        if busqueda:
            queryset = Medico.objects.filter(
                Q(usuario__cedula__icontains= busqueda)|
                Q(usuario__email__icontains= busqueda)|
                Q(usuario__first_name__icontains= busqueda)|
                Q(usuario__last_name__icontains= busqueda)
                ).distinct().order_by("pk")
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Médicos"
        return context

class MedicoCreateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'covid.add_medico'
    model = Medico
    form_class = MedicoForm
    second_form_class = UserForm
    template_name = "medico/medico_crear.html"
    success_url = reverse_lazy('medico_listar')
    success_message = 'Registro Guardado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Médicos"
        
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
            
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
       
        
        if  form.is_valid() and form2.is_valid():
            form2.instance.is_active= True
            form2.instance.username = form2.cleaned_data['cedula']
            form2.instance.password = make_password(form2.cleaned_data['cedula'])
            Medico = form.save(commit = False)
            grupo = Group.objects.get(name="Médico")
           
            Medico.usuario = form2.save()
            Medico.usuario.groups.add(grupo) 
            Medico.save()
            return HttpResponseRedirect(self.get_success_url())
        else :
            return self.render_to_response(self.get_context_data(form=form,form2=form2))
    
class MedicoUpdateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'covid.change_medico'
    model = Medico
    second_model = User
    form_class = MedicoForm
    second_form_class = UserForm
    template_name = "medico/medico_editar.html"
    success_url = reverse_lazy('medico_listar')
    success_message = 'Registro Editado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Médicos"
        pk = self.kwargs.get('pk',0)
        Medico = self.model.objects.get(id=pk)
        Usuario = self.second_model.objects.get(id=Medico.usuario_id) 
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=Usuario)
        context['id'] = pk 
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_medico = kwargs['pk'] 
        Medico = self.model.objects.get(id=id_medico)
        Usuario = self.second_model.objects.get(id=Medico.usuario_id)
        
        form = self.form_class(request.POST, instance = Medico)
        form2 = self.second_form_class(request.POST, instance = Usuario)
    
        
        if  form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            grupo = Group.objects.get(name="Medico")
            Usuario.groups.add(grupo) 
            Usuario.save()
            return HttpResponseRedirect(self.get_success_url())
        else :
            return HttpResponseRedirect(self.get_success_url())
        
class MedicoDeleteView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'covid.delete_medico'
    model = Medico
    template_name = "medico/medico_eliminar.html"
    success_url = reverse_lazy('medico_listar')
    success_message = 'Registro Eliminado Exitosamente'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            error_messeage =  "Este registro no puede ser eliminado!!"
            messages.success(self.request,error_messeage)
            return HttpResponseRedirect(success_url)
     
        return HttpResponseRedirect(success_url)

class MedicoDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'covid.view_medico'
    model = Medico
    template_name = "medico/medico_detalle.html"

#PACIENTE
class PacienteListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'covid.view_paciente'
    model = Paciente
    paginate_by = 7
    template_name = "paciente/paciente_listar.html"
    
    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")
        queryset = Paciente.objects.all().order_by("pk")
        if busqueda:
            queryset = Paciente.objects.filter(
                Q(usuario__cedula__icontains= busqueda)|
                Q(usuario__email__icontains= busqueda)|
                Q(usuario__first_name__icontains= busqueda)|
                Q(usuario__last_name__icontains= busqueda)
                ).distinct().order_by("pk")
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Pacientes"
        return context

class PacienteCreateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'covid.add_paciente'
    model = Paciente
    form_class = PacienteForm
    second_form_class = UserForm
    template_name = "paciente/paciente_crear.html"
    success_url = reverse_lazy('paciente_listar')
    success_message = 'Registro Guardado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Pacientes"
        
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
            
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
    
        
        if  form.is_valid() and form2.is_valid():
            form2.instance.is_active= True
            form2.instance.username = form2.cleaned_data['cedula']
            form2.instance.password = make_password(form2.cleaned_data['cedula'])
            Paciente = form.save(commit = False)
            grupo = Group.objects.get(name="Paciente")
            
            Paciente.usuario = form2.save()
            Paciente.usuario.groups.add(grupo) 
            Paciente.save()
            return HttpResponseRedirect(self.get_success_url())
        else :
            return self.render_to_response(self.get_context_data(form=form,form2=form2))
        
    
    
class PacienteUpdateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'covid.change_paciente'
    model = Paciente
    second_model = User
    form_class = PacienteForm
    second_form_class = UserForm
    template_name = "paciente/paciente_editar.html"
    success_url = reverse_lazy('paciente_listar')
    success_message = 'Registro Editado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Pacientes"
        pk = self.kwargs.get('pk',0)
        Paciente = self.model.objects.get(id=pk)
        Usuario = self.second_model.objects.get(id=Paciente.usuario_id)
        
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=Usuario)
        context['id'] = pk 
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_paciente = kwargs['pk'] 
        Paciente = self.model.objects.get(id=id_paciente)
        Usuario = self.second_model.objects.get(id=Paciente.usuario_id)
        
        form = self.form_class(request.POST, instance = Paciente)
        form2 = self.second_form_class(request.POST, instance = Usuario)
    
        
        if  form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            grupo = Group.objects.get(name="Paciente")
            Usuario.groups.add(grupo) 
            Usuario.save()
            return HttpResponseRedirect(self.get_success_url())
        else :
            return HttpResponseRedirect(self.get_success_url())
        
class PacienteDeleteView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'covid.delete_paciente'
    model = Paciente
    template_name = "paciente/paciente_eliminar.html"
    success_url = reverse_lazy('paciente_listar')
    success_message = 'Registro Eliminado Exitosamente'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            error_messeage =  "Este registro no puede ser eliminado!!"
            messages.success(self.request,error_messeage)
            return HttpResponseRedirect(success_url)
     
        return HttpResponseRedirect(success_url)

class PacienteDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'covid.view_paciente'
    model = Paciente
    template_name = "paciente/paciente_detalle.html"

#REPORTE ESTADISTI
class ReportView(LoginRequiredMixin,PermissionRequiredMixin,TemplateView):
    permission_required = 'covid.see_view_report'
    template_name = "reporte/reportes.html"
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        
        busqueda = self.request.GET.get("year")
        context['titulo'] ="Reportes estadísticos Covid-19"
        if busqueda:
            anio= busqueda
            context['anio'] =  "REPORTE: AÑO-"+ anio
            context['positivos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__year =anio,).count()
            context['negativo'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__year =anio,).count()
            context['positivosMasc'] = Analisis_Radiografico.objects.filter(result_analisis = 0,paciente__usuario__genero = 'M',fecha__year =anio,).count()
            context['negativoMasc'] = Analisis_Radiografico.objects.filter(result_analisis = 1,paciente__usuario__genero = 'M',fecha__year =anio,).count()
            context['positivosFem'] = Analisis_Radiografico.objects.filter(result_analisis = 0,paciente__usuario__genero = 'F',fecha__year =anio,).count()
            context['negativoFem'] = Analisis_Radiografico.objects.filter(result_analisis = 1,paciente__usuario__genero = 'F',fecha__year =anio,).count()
            context['total'] = Analisis_Radiografico.objects.filter(fecha__year =anio,).count()

            
            context['eneroPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__year =anio,fecha__month ='01',).count()
            context['eneroNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__year =anio,fecha__month ='01',).count()
            
            context['febPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__year =anio,fecha__month ='02',).count()
            context['febNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__year =anio,fecha__month ='02',).count()
            
            context['marzPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__year =anio,fecha__month ='03',).count()
            context['marzNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__year =anio,fecha__month ='03',).count()
        
            context['abrilPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__year =anio,fecha__month ='04',).count()
            context['abrilNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__year =anio,fecha__month ='04',).count()
        
            context['mayPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__year =anio,fecha__month ='05',).count()
            context['mayNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__year =anio,fecha__month ='05',).count()
        
            context['junioPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__year =anio,fecha__month ='06',).count()
            context['junioNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__year =anio,fecha__month ='06',).count()
            
            context['julioPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__year =anio,fecha__month ='07',).count()
            context['julioNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__year =anio,fecha__month ='07',).count()
            
            context['agostPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__year =anio,fecha__month ='08',).count()
            context['agostNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__year =anio,fecha__month ='08',).count()
            
            context['septPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__year =anio,fecha__month ='09',).count()
            context['septNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__year =anio,fecha__month ='09',).count()
            
            context['octPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__year =anio,fecha__month ='10',).count()
            context['octNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__year =anio,fecha__month ='10',).count()
            
            context['novPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__year =anio,fecha__month ='11',).count()
            context['novNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__year =anio,fecha__month ='11',).count()
            
            context['dicPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__year =anio,fecha__month ='12',).count()
            context['dicNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__year =anio,fecha__month ='12',).count()
        else:
            context['anio'] ='REPORTE: AÑO-ALL'
            context['positivos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,).count()
            context['negativo'] = Analisis_Radiografico.objects.filter(result_analisis = 1,).count()
            context['positivosMasc'] = Analisis_Radiografico.objects.filter(result_analisis = 0,paciente__usuario__genero = 'M',).count()
            context['negativoMasc'] = Analisis_Radiografico.objects.filter(result_analisis = 1,paciente__usuario__genero = 'M',).count()
            context['positivosFem'] = Analisis_Radiografico.objects.filter(result_analisis = 0,paciente__usuario__genero = 'F',).count()
            context['negativoFem'] = Analisis_Radiografico.objects.filter(result_analisis = 1,paciente__usuario__genero = 'F',).count()
            context['total'] = Analisis_Radiografico.objects.all().count()

            
            context['eneroPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__month ='01',).count()
            context['eneroNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__month ='01',).count()
            
            context['febPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__month ='02',).count()
            context['febNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__month ='02',).count()
            
            context['marzPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__month ='03',).count()
            context['marzNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__month ='03',).count()
        
            context['abrilPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__month ='04',).count()
            context['abrilNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__month ='04',).count()
        
            context['mayPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__month ='05',).count()
            context['mayNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__month ='05',).count()
        
            context['junioPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__month ='06',).count()
            context['junioNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__month ='06',).count()
            
            context['julioPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__month ='07',).count()
            context['julioNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__month ='07',).count()
            
            context['agostPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__month ='08',).count()
            context['agostNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__month ='08',).count()
            
            context['septPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__month ='09',).count()
            context['septNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__month ='09',).count()
            
            context['octPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__month ='10',).count()
            context['octNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__month ='10',).count()
            
            context['novPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__month ='11',).count()
            context['novNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__month ='11',).count()
            
            context['dicPos'] = Analisis_Radiografico.objects.filter(result_analisis = 0,fecha__month ='12',).count()
            context['dicNeg'] = Analisis_Radiografico.objects.filter(result_analisis = 1,fecha__month ='12',).count()
            
            
        
        
        
        return context

#ANALISIS RADIOGRAFICO
def predict(file):
    #modelo = os.path.join(settings.CNN_ROOT,'plugins\cnnModelo\modelo8.h5')
    #pesos = os.path.join(settings.CNN_ROOT,'plugins\cnnModelo\pesos8.h5')
    #print(modelo)
    #print(pesos)
    #cnn = load_model(r"C:\Users\User\Desktop\TRABAJO\TITULACION\app_covid\app_covid\static\plugins\cnnModelo\modelo8.h5")
    #cnn.load_weights(r"C:\Users\User\Desktop\TRABAJO\TITULACION\app_covid\app_covid\static\plugins\cnnModelo\pesos8.h5")
    #cnn = load_model(modelo)
    #cnn.load_weights(pesos)
    #longitud, altura = 200,200 
    #x = load_img(file, target_size=(longitud, altura))
    #x = img_to_array(x)
    #x = np.expand_dims(x, axis=0)
    #arreglo = cnn.predict(x) ##arreglo de 2 dimensiones [[1,0,0]]
    #resultado = arreglo[0]
    #respuesta = np.argmax(resultado)
    #if respuesta==1:
    #    print('Sin covid')
    #elif respuesta ==0:
    #    print('covid detectado')
    #return respuesta
    return 1

class RayxListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'covid.view_analisis_radiografico'
    model = Analisis_Radiografico
    paginate_by = 7
    template_name = "analisis/analisis_listar.html"

    def get_queryset(self):
        id_usuario = self.request.user.id
        busqueda = self.request.GET.get("buscar")
        usuario  = User.objects.get(pk=id_usuario)
        grupos = usuario.groups.all()
        for dato in grupos:
            if str(dato) == 'Médico':
                if busqueda:
                    queryset = Analisis_Radiografico.objects.filter( 
                                                                    Q(paciente__usuario__first_name__icontains= busqueda) |
                                                                    Q(paciente__usuario__last_name__icontains= busqueda)
                                                                    ).filter(doctor__usuario__id= id_usuario).distinct().order_by("pk")
                else:
                    queryset = Analisis_Radiografico.objects.filter(doctor__usuario =usuario.pk ).order_by("pk")
        if usuario.is_superuser:
            if busqueda:
                    queryset = Analisis_Radiografico.objects.filter( 
                                                                    Q(paciente__usuario__first_name__icontains= busqueda) |
                                                                    Q(paciente__usuario__last_name__icontains= busqueda)
                                                                    ).distinct().order_by("pk")
            else:
                queryset = Analisis_Radiografico.objects.all().order_by("pk") 
           
              
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Analisis rádiograficos"
        return context

class RayxCreateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'covid.add_analisis_radiografico'
    model = Analisis_Radiografico
    initial = {'doctor': '1'
               }
    form_class = RayxForm
    template_name = "analisis/analisis_crear.html"
    success_url = reverse_lazy('rayx_listar')
    success_message = 'Registro Guardado Exitosamente'
    
    def cal_edad(self):
        id_paciente = self.request.POST['paciente']
        usuario = Paciente.objects.get(id=id_paciente)
        
        edad = date.today().year-usuario.fec_nac.year
        if((date.today().month,date.today().day)<(usuario.fec_nac.month,usuario.fec_nac.day)):
            edad -=1
        return edad
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Analisis radiográficos"
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.edad= self.cal_edad()
        imagen = form.cleaned_data['imagen']
        ruta = os.path.join(settings.MEDIA_ROOT,'muestra_covid')
        file = os.path.join(ruta,str(imagen))
        form.instance.result_analisis = predict(file)   
        return super().form_valid(form) 
    
class RayxDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = ('covid.view_analisis_radiografico')
    model = Analisis_Radiografico
    template_name = "analisis/analisis_detalle.html"

class RayxDeleteView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'covid.delete_analisis_radiografico'
    model = Analisis_Radiografico
    template_name = "analisis/analisis_eliminar.html"
    success_url = reverse_lazy('rayx_listar')
    success_message = 'Registro Eliminado Exitosamente'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            error_messeage =  "Este registro no puede ser eliminado!!"
            messages.success(self.request,error_messeage)
            return HttpResponseRedirect(success_url)
     
        return HttpResponseRedirect(success_url)
    
class RayxUpdateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'covid.change_analisis_radiografico'
    model = Analisis_Radiografico
    form_class = RayxForm
    template_name = "analisis/analisis_editar.html"
    success_url = reverse_lazy('rayx_listar')
    success_message = 'Registro Editado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Analisis radiográficos"
        return context

#ANALISIS RESULTADO VISIBLE SOLO PARA EL PROPIO PACIENTE
class MyresultListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'covid.see_view_Analisis_paciente_only'
    model = Analisis_Radiografico
    paginate_by = 7
    template_name = "analisis/analisisPorPaciente_listar.html"

    def get_queryset(self):
        id_usuario = self.request.user.id
        usuario  = User.objects.get(pk=id_usuario)
        grupos = usuario.groups.all()
        for dato in grupos:
            if str(dato) == 'Paciente':
                queryset = Analisis_Radiografico.objects.filter(paciente__usuario =usuario.pk ).order_by("pk")
            
        if usuario.is_superuser:
            queryset = Analisis_Radiografico.objects.all().order_by("pk")   
        return queryset

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Resultado de Mis Radiografias"
        return context

class MyresultRayxDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = ( 'covid.see_view_Analisis_paciente_only',)
    model = Analisis_Radiografico
    template_name = "analisis/analisisPorPaciente_detalle.html"
    
#VACUNA  
class VacunaListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'covid.view_vacuna'
    model = Vacuna
    paginate_by = 7
    template_name = "vacuna/vacuna_listar.html"

    def get_queryset(self):
        busqueda = self.request.GET.get("buscar")
        queryset = Vacuna.objects.all().order_by("pk")
        if busqueda:
            queryset = Vacuna.objects.filter(
                Q(descripcion__icontains= busqueda)
                ).distinct().order_by("pk")
        return queryset


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Vacunas"
        return context

class VacunaCreateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'covid.add_vacuna'
    model = Vacuna
    form_class = VacunaForm
    template_name = "vacuna/vacuna_crear.html"
    success_url = reverse_lazy('vacuna_listar')
    success_message = 'Registro Guardado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Vacunas"
        return context

class VacunaUpdateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'covid.change_vacuna'
    model = Vacuna
    form_class = VacunaForm
    template_name = "vacuna/vacuna_editar.html"
    success_url = reverse_lazy('vacuna_listar')
    success_message = 'Registro Editado Exitosamente'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['titulo'] = "Registro de Vacunas"
        return context

class VacunaDeleteView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    permission_required = 'covid.delete_vacuna'
    model = Vacuna
    template_name = "vacuna/vacuna_eliminar.html"
    success_url = reverse_lazy('vacuna_listar')
    success_message = 'Registro Eliminado Exitosamente'
    
    
    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            
            self.object.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            error_messeage =  "Este registro no puede ser eliminado!!"
            messages.success(self.request,error_messeage)
            return HttpResponseRedirect(success_url)
     
        return HttpResponseRedirect(success_url)
    
class VacunaDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'covid.view_vacuna'
    model = Vacuna
    template_name = "vacuna/vacuna_detalle.html"
