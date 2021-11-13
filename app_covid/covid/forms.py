#DJANGO
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

#MODELS
from .models import Menu,Group,Permission,User,Menu_Groups,Vacuna, EspecialidadMedico,Medico,Paciente,Analisis_Radiografico
from crum import get_current_user
class MenuForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            self.fields['grupo'].widget.attrs['class'] = "duallistbox"
            visible.field.widget.attrs['class'] = 'form-control form-control  form-row ' 
    class Meta:
        model = Menu
        fields = '__all__'
        exclude=("usuario_creacion","usuario_modificacion",)
        
           
class GrupoForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GrupoForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = "form-control"
        self.fields['permissions'].widget.attrs['class'] = "duallistbox"
        self.fields['permissions'].queryset = Permission.objects.exclude(content_type__model__in=['session', 'usuarios', 'permission', 'contenttype', 'logentry', 'configuracion'])
            
class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
        exclude=("password","last_login","user_permissions","date_joined","username",)


    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            self.fields['groups'].widget.attrs['class'] = "duallistbox"
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['genero'].widget.attrs['class'] = "form-control select"
    
class MenuGrupoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MenuGrupoForm, self).__init__(*args, **kwargs)
    
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '

    class Meta:
        model = Menu_Groups
        fields = '__all__'
        exclude=("group","menu",)
            
class PerfilForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
    
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
    class Meta:
        model = User
        fields = '__all__'
        exclude=("password","last_login","user_permissions","date_joined","username","groups","is_active","is_staff","is_superuser")
       
class CambiarContraseñaForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
                # Le añadimos clases CSS a los inputs
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '

class EspecialidadMedicoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EspecialidadMedicoForm, self).__init__(*args, **kwargs)
    
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
            
    class Meta:
        model = EspecialidadMedico
        fields = '__all__'
        
class MedicoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MedicoForm, self).__init__(*args, **kwargs)
    
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
            self.fields['especialidad'].widget.attrs['class'] = "form-control select"
            
    class Meta:
        model = Medico
        fields = '__all__'
        exclude= ('usuario',)
        
class PacienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
    
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
            self.fields['es_vacunado'].widget.attrs['onclick'] = "ocultarCampos()"
           
            
    class Meta:
        model = Paciente
        fields = '__all__'
        exclude= ('usuario',)
      


class RayxForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RayxForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
            self.fields['paciente'].widget.attrs['class'] = "form-control select"
            self.fields['doctor'].widget.attrs['class'] = "form-control select"
        user = get_current_user()  
        id_usuario = user.pk
        usuario  = User.objects.get(pk=id_usuario)
        grupos = usuario.groups.all()
        for dato in grupos:
            if str(dato) == 'Médico':      
                self.fields['doctor'].queryset =  Medico.objects.filter(usuario=user.pk)
  
    class Meta:
        model = Analisis_Radiografico
        fields = '__all__'
     


class VacunaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VacunaForm, self).__init__(*args, **kwargs)
    
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
            
    class Meta:
        model = Vacuna
        fields = '__all__'
    
    
