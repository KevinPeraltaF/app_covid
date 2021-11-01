#DJANGO
from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Permission
from django.core import signing
#auditoria - crum django
from crum import get_current_user

#MODELO BASE - CLASE ABSTRACTA
class ModeloBase(models.Model):
    class Meta:
        """Meta definition for ModeloBase."""
        abstract = True


    """Model definition for ModeloBase."""
    fecha_creacion = models.DateTimeField(verbose_name='Fecha creación',auto_now_add=True)
    usuario_creacion = models.ForeignKey(User, verbose_name='Usuario Creación', related_name='+', blank=True, null=True,on_delete=models.PROTECT, editable=False)
    usuario_modificacion = models.ForeignKey(User, verbose_name='Usuario Modificación', related_name='+', blank=True, null=True,on_delete=models.PROTECT , editable=False)
    fecha_modificacion = models.DateTimeField(verbose_name='Fecha Modificación', auto_now=True)
    estado = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_creacion = user
        self.usuario_modificacion = user
        super(ModeloBase, self).save(*args, **kwargs)

   

    

#MODELO MENU 
class Menu(ModeloBase):
    """Model definition for Menu."""
    titulo = models.CharField(verbose_name='Título',max_length=200)
    descripcion = models.CharField( verbose_name='Descripciòn',max_length=200)
    icono = models.ImageField(verbose_name="icono", upload_to='icon/')
    url = models.CharField(verbose_name='Url', max_length=200)
    es_modulo_principal = models.BooleanField(default=False ,verbose_name='¿Es módulo principal?')
    principal = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    grupo = models.ManyToManyField(Group, verbose_name='Grupos de usuario')
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

  


#MODELO PERFIL_USUARIO - MENU
class MenuGrupo(ModeloBase):
    menu = models.ForeignKey(Menu, verbose_name='Menù', on_delete=models.CASCADE)
    grupo_usuario = models.ManyToManyField(Group, verbose_name='Grupo Usuario')

    class Meta:
        verbose_name = "Menú Perfil"
        verbose_name_plural = "Menú Perfiles"

    def __str__(self):
        return '{}'.format(self.menu.nombre)
