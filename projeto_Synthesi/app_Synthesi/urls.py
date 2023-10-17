from django.urls import path
from . import views


urlpatterns = [
    path('', views.pagina_inicio, name='inicio'),
    path('login/', views.pagina_login, name='login'),
    path('cadastro/', views.pagina_cadastro, name='cadastro'),
    path('salas/', views.pagina_salas, name='salas'),
    path('monitoramento/', views.pagina_monitoramento, name='monitoramento'),
    path('presenca/', views.pagina_presenca, name='presenca'),
    path('musica/', views.pagina_musica, name='musica'),
    path('autoavaliacao/', views.pagina_autoavaliacao, name='autoavaliacao'),    
]