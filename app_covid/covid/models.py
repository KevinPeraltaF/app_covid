#DJANGO

from django.db import models
from django.contrib.auth.models import Group, AbstractUser, Permission
from django.conf import settings


import os
from django.db.models.signals import pre_delete, post_delete, pre_save
from django.dispatch import receiver


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
    estado_registro = models.BooleanField(verbose_name="Estado del registro",default=True)
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_creacion = user
        self.usuario_modificacion = user
        super(ModeloBase, self).save(*args, **kwargs)




class User(AbstractUser,ModeloBase):
    cedula=models.CharField(max_length=10, verbose_name='Cédula', unique = True)
    tipo_genero = (('M', 'Masculino'), ('F', 'Femenino'))
    genero = models.CharField('Género', choices=tipo_genero, default='M', max_length=1)
    
    def get_full_name(self):
        """Unicode representation of Analisis_Radiografico."""
        return '{} {}'.format(self.last_name,self.first_name)

#Especialidad
class EspecialidadMedico(ModeloBase):
    descripcion = models.CharField("Especialidad", max_length=200 , unique=True)
     
    def __str__(self):
        """Unicode representation of EspecialidadMedico."""
        return '{}'.format(self.descripcion)
    
    def save(self, *args, **kwargs):
        """Save method for Analisis_Radiografico."""
        self.descripcion = self.descripcion.lower().strip()
        return super(EspecialidadMedico, self).save(*args, **kwargs)
    
    
#vacuna
class Vacuna(ModeloBase):
    descripcion = models.CharField("Vacuna", max_length=200 , unique=True)
     
    def __str__(self):
        """Unicode representation of EspecialidadMedico."""
        return '{}'.format(self.descripcion)
    
    def save(self, *args, **kwargs):
        """Save method for Analisis_Radiografico."""
        self.descripcion = self.descripcion.lower().strip()
        return super(Vacuna, self).save(*args, **kwargs)
  
#MEDICO
class Medico(ModeloBase):      
        
    usuario  = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Usuario",on_delete=models.PROTECT)
    especialidad = models.ForeignKey(EspecialidadMedico, verbose_name="Especialidad", on_delete=models.PROTECT)
    def __str__(self):
        """Unicode representation of Analisis_Radiografico."""
        return '{}'.format(self.usuario.get_full_name())
    
    class Meta:
        '''Meta doctor'''
        permissions = (
            ("see_view_report", "Can_view_report"),
        )
         
# PACIENTE
class Paciente(ModeloBase):
     usuario  = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="Usuario",on_delete=models.PROTECT)
     direccion = models.CharField("Dirección", max_length=200,blank=True )
     es_vacunado = models.BooleanField(verbose_name="¿Está usted vacunado contra el covid?" )
     vacuna = models.ForeignKey(Vacuna, verbose_name="Tipo de Vacuna", on_delete=models.PROTECT,null=True,blank=True)
     Diagnostico = models.TextField(verbose_name="Diágnostico previo",null=True, blank=True)
     def __str__(self):
        """Unicode representation of Analisis_Radiografico."""
        return '{} CI: {}'.format(self.usuario.get_full_name(),self.usuario.cedula)
    
     def save(self, *args, **kwargs):
        """Save method for Analisis_Radiografico."""
        self.direccion = self.direccion.lower().strip()
        return super(Paciente, self).save(*args, **kwargs)

#MODELO MENU 
class Menu(ModeloBase):
    """Model definition for Menu."""
    titulo = models.CharField(verbose_name='Título',max_length=200)
    descripcion = models.CharField( verbose_name='Descripciòn',max_length=200)
    icono = models.ImageField(verbose_name="icono", upload_to='icon/')
    url = models.CharField(verbose_name='Url', max_length=200)
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
    
@receiver(post_delete, sender=Menu)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem when corresponding `MediaFile` object
        is deleted."""
    ruta = settings.MEDIA_ROOT +"\\"+ str(instance.icono)
    if ruta:
        if os.path.isfile(ruta):
            os.remove(ruta)
                           
@receiver(pre_save, sender=Menu)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes old file from filesystem when corresponding `MediaFile`
        object is updated with new file."""
    if not instance.pk:
         return False
    if not instance.pk:
        return False

    try:
        old_file = Menu.objects.get(pk=instance.pk).icono
    except Menu.DoesNotExist:
        return False

    new_file = instance.icono
    if not old_file == new_file:
        ruta = settings.MEDIA_ROOT +"\\"+ str(old_file)
        if os.path.isfile(ruta):
            os.remove(ruta)
                
class Menu_Groups(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

  
class Analisis_Radiografico(ModeloBase):
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE, related_name="paciente_user")
    doctor = models.ForeignKey(Medico,on_delete=models.CASCADE, related_name="doctor_user")
    imagen = models.ImageField(verbose_name="Imagen de Rayos X", upload_to='muestra_covid/')
    result_analisis=models.BooleanField(verbose_name="Libre de Covid" )
    fecha = models.DateTimeField(verbose_name='Fecha de Registro', auto_now_add=True)
    descripcion = models.CharField(verbose_name='Descripcion', max_length=200)
    class Meta:
        """Meta definition for Analisis_Radiografico."""
        verbose_name = 'Analisis'
        verbose_name_plural = 'Analisis'
        
        permissions = (
            ("see_view_Analisis_paciente_only", "Can_view_Analisis_paciente_only"),
        )
         
        

    def __str__(self):
        """Unicode representation of Analisis_Radiografico."""
        return '{}'.format(self.paciente)
    
    def save(self, *args, **kwargs):
        """Save method for Analisis_Radiografico."""
        self.descripcion = self.descripcion.lower().strip()
        return super(Analisis_Radiografico, self).save(*args, **kwargs)

@receiver(post_delete, sender=Analisis_Radiografico)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem when corresponding `MediaFile` object
        is deleted."""
    ruta = settings.MEDIA_ROOT +"\\"+ str(instance.imagen)
    if ruta:
        if os.path.isfile(ruta):
            os.remove(ruta)
                           
@receiver(pre_save, sender=Analisis_Radiografico)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes old file from filesystem when corresponding `MediaFile`
        object is updated with new file."""
    if not instance.pk:
         return False
    if not instance.pk:
        return False

    try:
        old_file = Analisis_Radiografico.objects.get(pk=instance.pk).imagen
    except Menu.DoesNotExist:
        return False

    new_file = instance.imagen
    if not old_file == new_file:
        ruta = settings.MEDIA_ROOT +"\\"+ str(old_file)
        if os.path.isfile(ruta):
            os.remove(ruta)
  


