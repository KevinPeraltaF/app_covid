#DJANGO
from django import forms
#MODELS
from .models import Menu,Group,Permission,User

class MenuForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        
        self.fields["principal"].queryset = Menu.objects.filter(es_modulo_principal=True, principal__isnull= True)
        
        for visible in self.visible_fields():
            self.fields['grupo'].widget.attrs['class'] = "duallistbox"
            visible.field.widget.attrs['class'] = 'form-control '
    class Meta:
        model = Menu
        fields = '__all__'
        
    
        exclude=("usuario_creacion","usuario_modificacion","estado",)
           
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
    
    
   
            

        
