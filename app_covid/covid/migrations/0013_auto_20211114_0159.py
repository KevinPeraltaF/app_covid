# Generated by Django 3.2.9 on 2021-11-14 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0012_alter_analisis_radiografico_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='especialidadmedico',
            name='estado_registro',
            field=models.BooleanField(default=True, verbose_name='Estado del registro'),
        ),
        migrations.AddField(
            model_name='medico',
            name='estado_registro',
            field=models.BooleanField(default=True, verbose_name='Estado del registro'),
        ),
        migrations.AddField(
            model_name='menu',
            name='estado_registro',
            field=models.BooleanField(default=True, verbose_name='Estado del registro'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='estado_registro',
            field=models.BooleanField(default=True, verbose_name='Estado del registro'),
        ),
        migrations.AddField(
            model_name='user',
            name='estado_registro',
            field=models.BooleanField(default=True, verbose_name='Estado del registro'),
        ),
        migrations.AddField(
            model_name='vacuna',
            name='estado_registro',
            field=models.BooleanField(default=True, verbose_name='Estado del registro'),
        ),
    ]
