#DJANGO
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.forms.forms import Form
from django.forms.models import inlineformset_factory
#MODELS
from .models import Menu,Group,Permission,User,Menu_Groups, EspecialidadMedico,Medico,Paciente

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
        field_order = ['is_active', 'is_staff','is_superuser',]
           
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
    class Meta:
        model = Medico
        fields = '__all__'
        exclude= ('usuario',)
        
class PacienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
    
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
    class Meta:
        model = Paciente
        fields = '__all__'
        exclude= ('usuario',)
      
      



   
    
    
