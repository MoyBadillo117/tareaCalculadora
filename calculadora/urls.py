from django.urls import path
from . import views #para importar la clase vista en el directorio actual

urlpatterns = {
    path('', views.index, name ='index'),
    path('procesamiento', views.procesamiento, name="procesamiento"),
    path('lista',views.lista,name='lista'),
    path('suma',views.suma,name='suma'),
    path('resta',views.resta,name='resta'),
    path('multiplicacion',views.multiplicacion,name='multiplicacion'),
    path('division',views.divison,name='division'),
    path('usuarios',views.usuarios,name='usuarios'),
    path('usuarios_p',views.usuarios_p,name='usuarios_p'),
    path('usuarios_d',views.usuarios_d,name='usuarios_d'),
    
}