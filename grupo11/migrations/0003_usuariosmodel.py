# Generated by Django 5.0.4 on 2025-03-24 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupo11', '0002_alter_animalmodel_anim_caracteristicas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuariosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('is_admin', models.BooleanField()),
            ],
        ),
    ]
