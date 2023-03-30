from rest_framework import serializers
from . models import Reto,Jugadores,Usuarios,Partida_Jugadores

class RetoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reto
        fields = ('id','nombre','minutos_jugados')

class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jugadores
        fields = ('id','grupo','num_lista')

class UsuariosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id','password')

class Partida_JugadoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Partida_Jugadores
        fields = ('id','fecha','id_usuario','minutos_jugados','puntaje')