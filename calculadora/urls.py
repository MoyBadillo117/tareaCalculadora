from django.urls import include,path
from rest_framework import routers
from . import views 
app_name = 'calculadora'
router = routers.DefaultRouter()
router.register(r'reto', views.RetoViewSet)
router.register(r'jugador', views.JugadoresViewSet)

urlpatterns = [
    path('api',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',views.index, name='index'),
    path('procesamiento', views.procesamiento, name='procesamiento'),
    path('lista',views.lista,name='lista'),
    path('score',views.score,name='score'),
    path('usuarios',views.usuarios,name='usuarios'),
    path('usuarios_p',views.usuarios_p,name='usuarios_p'),
    path('usuarios_d',views.usuarios_d, name='usuarios_d'),
    path('login', views.login, name='login'),
    path('procesologin', views.procesologin, name='procesologin'),
    path('valida_usuario',views.valida_usuario,name='valida_usuario'),
    path('grafica',views.grafica,name='grafica'),
    path('barras',views.barras,name='barras'),
    path('Menu',views.Menu,name='Menu'), 
    path('visualizarUsuarios',views.visualizarUsuarios,name='visualizarUsuarios'),
    path('añadirUsuario',views.añadirUsuario,name='añadirUsuario'), 
    path('usuarioAñadido',views.usuarioAñadido,name='usuarioAñadido'),
    path('eliminarUsuario',views.eliminarUsuario,name='eliminarUsuario'), 
    path('usuarioEliminado',views.usuarioEliminado,name='usuarioEliminado'),
]