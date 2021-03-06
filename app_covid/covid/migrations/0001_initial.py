# Generated by Django 3.2.9 on 2021-12-04 15:59

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creaci??n')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificaci??n')),
                ('estado_registro', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='C??dula')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1, verbose_name='G??nero')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('usuario_creacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creaci??n')),
                ('usuario_modificacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificaci??n')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='EspecialidadMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creaci??n')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificaci??n')),
                ('estado_registro', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('descripcion', models.CharField(max_length=200, unique=True, verbose_name='Especialidad')),
                ('usuario_creacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creaci??n')),
                ('usuario_modificacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificaci??n')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creaci??n')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificaci??n')),
                ('estado_registro', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('titulo', models.CharField(max_length=200, verbose_name='T??tulo')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripci??n')),
                ('icono', models.ImageField(upload_to='icon/', verbose_name='icono')),
                ('url', models.CharField(max_length=200, verbose_name='Url')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creaci??n')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificaci??n')),
                ('estado_registro', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('descripcion', models.CharField(max_length=200, unique=True, verbose_name='Vacuna')),
                ('usuario_creacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creaci??n')),
                ('usuario_modificacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificaci??n')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creaci??n')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificaci??n')),
                ('estado_registro', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('direccion', models.CharField(blank=True, max_length=200, verbose_name='Direcci??n')),
                ('es_vacunado', models.BooleanField(verbose_name='??Est?? usted vacunado contra el covid?')),
                ('Diagnostico', models.TextField(blank=True, null=True, verbose_name='Di??gnostico previo')),
                ('fec_nac', models.DateField(default=datetime.date.today, verbose_name='Fecha de Nacimiento')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('usuario_creacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creaci??n')),
                ('usuario_modificacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificaci??n')),
                ('vacuna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='covid.vacuna', verbose_name='Tipo de Vacuna')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Menu_Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covid.menu')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='grupo',
            field=models.ManyToManyField(through='covid.Menu_Groups', to='auth.Group', verbose_name='Grupos de usuario'),
        ),
        migrations.AddField(
            model_name='menu',
            name='usuario_creacion',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creaci??n'),
        ),
        migrations.AddField(
            model_name='menu',
            name='usuario_modificacion',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificaci??n'),
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creaci??n')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificaci??n')),
                ('estado_registro', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='covid.especialidadmedico', verbose_name='Especialidad')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('usuario_creacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creaci??n')),
                ('usuario_modificacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificaci??n')),
            ],
            options={
                'permissions': (('see_view_report', 'Can_view_report'),),
            },
        ),
        migrations.CreateModel(
            name='Analisis_Radiografico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creaci??n')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificaci??n')),
                ('estado_registro', models.BooleanField(default=True, verbose_name='Estado del registro')),
                ('imagen', models.ImageField(upload_to='muestra_covid/', verbose_name='Imagen de Rayos X')),
                ('result_analisis', models.BooleanField(verbose_name='Libre de Covid')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Registro')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctor_user', to='covid.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='paciente_user', to='covid.paciente')),
                ('usuario_creacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Creaci??n')),
                ('usuario_modificacion', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Modificaci??n')),
            ],
            options={
                'verbose_name': 'Analisis',
                'verbose_name_plural': 'Analisis',
                'permissions': (('see_view_Analisis_paciente_only', 'Can_view_Analisis_paciente_only'),),
            },
        ),
    ]
