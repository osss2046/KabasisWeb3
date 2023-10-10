# Generated by Django 4.2.5 on 2023-09-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutenticacionApp', '0005_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tipo_usuario',
            field=models.CharField(blank=True, choices=[('', 'Selecciona el tipo de usuario'), ('editor_contenido', 'Editor de contenido'), ('revisor', 'Revisor'), ('estudiante', 'Estudiante'), ('visualizador', 'Visualizador'), ('reporteria', 'Reporteria')], default='', max_length=20, verbose_name='Tipo de Usuario'),
        ),
    ]