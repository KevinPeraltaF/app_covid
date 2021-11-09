#DJANGO
from django.db import models
from django.contrib.auth.models import Group, AbstractUser, Permission
from django.conf import settings

#auditoria - crum django
from crum import get_current_user




#MODELO BASE - CLASE ABSTRACTA
class ModeloBase(models.Model):
    class Meta:
        """Meta definition for ModeloBase."""
        abstract = True


    """Model definition for ModeloBase."""
    fecha_creacion = models.DateTimeField(verbose_name='Fecha creación',auto_now_add=True)
    usuario_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario Creación', related_name='+', blank=True, null=True,on_delete=models.PROTECT, editable=False)
    usuario_modificacion = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario Modificación', related_name='+', blank=True, null=True,on_delete=models.PROTECT , editable=False)
    fecha_modificacion = models.DateTimeField(verbose_name='Fecha Modificación', auto_now=True)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_creacion = user
        self.usuario_modificacion = user
        super(ModeloBase, self).save(*args, **kwargs)


class User(AbstractUser,ModeloBase):
    cedula=models.CharField(max_length=10, verbose_name='Cédula')
    tipo_genero = (('N', 'Ninguno'), ('M', 'Masculino'), ('F', 'Femenino'))
    genero = models.CharField('Género', choices=tipo_genero, default='N', max_length=1)

#Especialidad
class EspecialidadMedico(ModeloBase):
     descripcion = models.CharField("Especialidad", max_length=200 , unique=True)

#MEDICO
class Medico(ModeloBase):
     usuario  = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Usuario",on_delete=models.PROTECT)
     especialidad = models.ForeignKey(EspecialidadMedico, verbose_name="Especialidad", on_delete=models.PROTECT)

# PACIENTE
class Paciente(ModeloBase):
     usuario  = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Usuario",on_delete=models.PROTECT)
     direccion = models.TextField("Dirección", max_length=200 )

#MODELO MENU 
class Menu(ModeloBase):
    """Model definition for Menu."""
    titulo = models.CharField(verbose_name='Título',max_length=200)
    descripcion = models.CharField( verbose_name='Descripciòn',max_length=200)
    icono = models.ImageField(verbose_name="icono", upload_to='icon/')
    url = models.CharField(verbose_name='Url', max_length=200)
    es_modulo_principal = models.BooleanField(default=False ,verbose_name='¿Es módulo principal?')
    principal = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    grupo = models.ManyToManyField(Group, through='Menu_Groups', verbose_name='Grupos de usuario')
    activo = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Menu."""
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        """Unicode representation of Menu."""
        return '{}'.format(self.titulo)
    
    def save(self, *args, **kwargs):
        """Save method for Menu."""
        self.titulo = self.titulo.lower().strip()
        self.descripcion = self.descripcion.lower().strip()
        return super(Menu, self).save(*args, **kwargs)

class Menu_Groups(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

  


