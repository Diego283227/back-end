from rest_framework import serializers
from .models import Inscritos, Institucion, Autor



class InstitucionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'


class InscritosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = '__all__'


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

  

     