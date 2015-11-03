from rest_framework import serializers
from .models import *

# Serializers define the API representation.
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('name', 'last_name',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    custom_user = UserDetailsSerializer()
    
    class Meta:
        model = CustomUser
        fields = ('id', 'custom_user','email_user','username',)
        
    
    def create(self, validated_data):
        custom_user_data = validated_data.pop('custom_user')
        custom = CustomUser.objects.create(**validated_data)
        UserDetails.objects.create(custom_user=custom, **custom_user_data)
        return custom
        
    def update(self, instance, validated_data):
        custom_user_data = validated_data.pop('custom_user')
        instance.custom_user = custom_user_data
        instance.custom_user.save()
        return instance
    
class TamanoCabelloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TamanoCabello
        fields = ('id','name','description',)
        read_only_fields = ('id',)
        
class RostroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rostro
        fields = ('id','name','description',)
        read_only_fields = ('id',)
        
class OcasionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ocasion
        fields = ('id','name','description',)
        read_only_fields = ('id',)
        
class TipoCabelloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoCabello
        fields = ('id','name','description',)
        read_only_fields = ('id',)
        
class MobileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mobile
        fields = ('id', 'company', 'number')
       

class PeinadoTamanoCabelloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TamanoCabello
        fields = ('id',)   
        
class PeinadoRostroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rostro
        fields = ('id',)   
        
class PeinadOcasionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ocasion
        fields = ('id',)  
        
class PeinadoTipoCabelloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoCabello
        fields = ('id',)   

class PeinadoPeluqueriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peluqueria
        fields = ('id',)
        
class SucursalPeluqueriaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sucursal
        fields = ('id',)
        
class PeluqueriaSerializer(serializers.HyperlinkedModelSerializer):
    peinados = PeinadoTamanoCabelloSerializer(many=True, read_only=True)
    sucursales = SucursalPeluqueriaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Peluqueria
        fields = ('id', 'name', 'ruc', 'peinados', 'sucursales',)
        
class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    peluqueria = PeinadoPeluqueriaSerializer(read_only=True)
    moviles = MobileSerializer(source='mobiles', many=True)
    
    class Meta:
        model = Sucursal
        fields = ('id', 'district', 'phone', 'moviles', 'latitud', 'longitud', 'peluqueria')

class PeinadoSerializer(serializers.HyperlinkedModelSerializer):
    tamanos_cabello = PeinadoTamanoCabelloSerializer(many=True, read_only=True)
    rostros = PeinadoRostroSerializer(many=True, read_only=True)
    ocasiones = PeinadOcasionSerializer(many=True, read_only=True)
    tipos_cabello = PeinadoTipoCabelloSerializer(many=True, read_only=True)
    peluqueria = PeinadoPeluqueriaSerializer(read_only=True)
    
    class Meta:
        model = Peinado
        fields = ('id', 'name', 'gender', 'dificulty', 'materials', 'image','tamanos_cabello', 'rostros', 'ocasiones', 'tipos_cabello', 'peluqueria')