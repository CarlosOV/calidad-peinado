# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(default=b'U', max_length=2, choices=[(b'A', b'Administrador Peluqueria'), (b'U', b'Usuario')])),
                ('email_user', models.EmailField(unique=True, max_length=140)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=1, verbose_name='empresa', choices=[(b'M', b'Movistar'), (b'C', b'Claro'), (b'E', b'Entel'), (b'B', b'Bitel')])),
                ('number', models.CharField(max_length=100, verbose_name='n\xfamero')),
            ],
        ),
        migrations.CreateModel(
            name='Ocasion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='nombre')),
                ('description', models.CharField(max_length=100, verbose_name='descripci\xf3n')),
            ],
            options={
                'verbose_name': 'ocasione',
            },
        ),
        migrations.CreateModel(
            name='Peinado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, verbose_name='nombre')),
                ('dificulty', models.CharField(max_length=1, verbose_name='difucltad', choices=[(b'F', 'F\xe1cil'), (b'D', 'Dif\xedcil')])),
                ('gender', models.CharField(max_length=1, verbose_name='sexo', choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('materials', models.TextField(verbose_name='material', blank=True)),
                ('image', models.ImageField(upload_to=b'peinados', verbose_name='imagen')),
                ('ocasiones', models.ManyToManyField(related_name='peinados', verbose_name='ocasiones', to='peinados.Ocasion')),
            ],
            options={
                'verbose_name': 'Peinado',
            },
        ),
        migrations.CreateModel(
            name='Peluqueria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45, verbose_name='nombre')),
                ('ruc', models.CharField(unique=True, max_length=11, verbose_name='ruc')),
            ],
            options={
                'verbose_name': 'Peluquer\xeda',
            },
        ),
        migrations.CreateModel(
            name='Rostro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='nombre')),
                ('description', models.CharField(max_length=100, verbose_name='descripci\xf3n')),
            ],
            options={
                'verbose_name': 'tipos de rostro',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('district', models.CharField(max_length=100, verbose_name='distrito')),
                ('phone', models.CharField(max_length=15, verbose_name='tel\xe9fono')),
                ('latitud', models.CharField(max_length=100, verbose_name='latitud')),
                ('longitud', models.CharField(max_length=100, verbose_name='longitud')),
                ('peluqueria', models.ForeignKey(related_name='sucursales', verbose_name='peluquer\xeda', to='peinados.Peluqueria')),
            ],
            options={
                'verbose_name': 'Sucursale',
            },
        ),
        migrations.CreateModel(
            name='TamanoCabello',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='nombre')),
                ('description', models.CharField(max_length=100, verbose_name='descripci\xf3n')),
            ],
            options={
                'verbose_name': 'tama\xf1os de cabello',
            },
        ),
        migrations.CreateModel(
            name='TipoCabello',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='nombre')),
                ('description', models.CharField(max_length=100, verbose_name='descripci\xf3n')),
            ],
            options={
                'verbose_name': 'tipos de cabello',
            },
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=45, verbose_name='nombre')),
                ('last_name', models.CharField(unique=True, max_length=45, verbose_name='apellido')),
                ('custom_user', models.OneToOneField(related_name='custom_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='peinado',
            name='peluqueria',
            field=models.ForeignKey(related_name='peinados', verbose_name='peluquer\xeda', to='peinados.Peluqueria'),
        ),
        migrations.AddField(
            model_name='peinado',
            name='rostros',
            field=models.ManyToManyField(related_name='peinados', verbose_name='rostros', to='peinados.Rostro'),
        ),
        migrations.AddField(
            model_name='peinado',
            name='tamanos_cabello',
            field=models.ManyToManyField(related_name='peinados', verbose_name='tama\xf1o de cabello', to='peinados.TamanoCabello'),
        ),
        migrations.AddField(
            model_name='peinado',
            name='tipos_cabello',
            field=models.ManyToManyField(related_name='peinados', verbose_name='tipos de cabello', to='peinados.TipoCabello'),
        ),
        migrations.AddField(
            model_name='mobile',
            name='sucursal',
            field=models.ForeignKey(related_name='mobiles', verbose_name='sucursal', to='peinados.Sucursal'),
        ),
    ]
