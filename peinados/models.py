# coding=utf8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class CustomUser(AbstractUser):
    type_choices = (
        ('A', 'Administrador Peluqueria'),
        ('U', 'Usuario'),
    )
    user_type = models.CharField(max_length=2,
                                 choices=type_choices,
                                 default='U')
    email_user = models.EmailField(max_length=140 , unique=True)  

class UserDetails(models.Model):
    custom_user = models.OneToOneField('CustomUser', related_name="custom_user")
    name =  models.CharField(u"nombre", max_length = 45, unique=True)
    last_name =  models.CharField(u"apellido", max_length = 45, unique=True)

    #USERNAME_FIELD = 'email_user'
    
class TamanoCabello(models.Model):
    name = models.CharField(u"nombre", max_length = 45, unique=True)
    description = models.CharField(u"descripción", max_length = 100)
    
    def __unicode__(self):
		return self.name
    
    class Meta:
         verbose_name = u"tamaños de cabello"
    
class Rostro(models.Model):
    name = models.CharField(u"nombre", max_length = 45, unique=True)
    description = models.CharField(u"descripción", max_length = 100)
    
    def __unicode__(self):
		return self.name
    
    class Meta:
         verbose_name = u"tipos de rostro"
    
class Ocasion(models.Model):
    name = models.CharField(u"nombre", max_length = 45, unique=True)
    description = models.CharField(u"descripción", max_length = 100)
    
    def __unicode__(self):
		return self.name
    
    class Meta:
         verbose_name = u"ocasione"

class TipoCabello(models.Model):
    name = models.CharField(u"nombre", max_length = 45, unique=True)
    description = models.CharField(u"descripción", max_length = 100)
    
    def __unicode__(self):
		return self.name
    
    class Meta:
         verbose_name = u"tipos de cabello"

class Peluqueria(models.Model):
    name = models.CharField(u"nombre", max_length = 45)
    ruc = models.CharField(u"ruc", max_length=11, unique=True)
    
    
    def __unicode__(self):
        return self.name
        
    class Meta:
         verbose_name = u"Peluquería"
      
class Peinado(models.Model):
    DIFICULTY_CHOICES = (
        ('F', u'Fácil'),
        ('D', u'Difícil'),
    )
    
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    name = models.CharField(u"nombre", max_length = 45)
    dificulty = models.CharField(u"difucltad", max_length=1, choices=DIFICULTY_CHOICES)
    gender = models.CharField(u"sexo", max_length=1, choices=GENDER_CHOICES)
    materials = models.TextField(u"material", blank=True)
    image = models.ImageField(u"imagen", upload_to = 'peinados')
    tamanos_cabello = models.ManyToManyField(TamanoCabello, verbose_name = u"tamaño de cabello", related_name="peinados")
    ocasiones = models.ManyToManyField(Ocasion, verbose_name = u"ocasiones", related_name="peinados")
    rostros = models.ManyToManyField(Rostro, verbose_name = u"rostros", related_name="peinados")
    tipos_cabello = models.ManyToManyField(TipoCabello, verbose_name = u"tipos de cabello", related_name="peinados")
    peluqueria = models.ForeignKey(Peluqueria, verbose_name = u"peluquería", related_name = "peinados")
    
    def __unicode__(self):
        return self.name
        
    class Meta:
         verbose_name = u"Peinado"
        
class Sucursal(models.Model):
    district = models.CharField(u"distrito", max_length = 100)
    phone = models.CharField(u"teléfono", max_length = 15)
    latitud = models.CharField(u"latitud", max_length = 100)
    longitud = models.CharField(u"longitud", max_length = 100)
    peluqueria = models.ForeignKey(Peluqueria, verbose_name = u"peluquería", related_name = "sucursales")
    
    def __unicode__(self):
		return self.district
    
    class Meta:
         verbose_name = u"Sucursale"

class Mobile(models.Model):
    
    MOBILE_CHOICES = (
        ('M', 'Movistar'),
        ('C', 'Claro'),
        ('E', 'Entel'),
        ('B', 'Bitel'),
    )
    
    sucursal = models.ForeignKey(Sucursal, verbose_name = u"sucursal", related_name="mobiles")
    company = models.CharField(u"empresa", max_length=1, choices=MOBILE_CHOICES)
    number = models.CharField(u"número", max_length = 100)
