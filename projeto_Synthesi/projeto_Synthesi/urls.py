from django.contrib import admin
from django.urls import path
from app_Synthesi import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicio, name='inicio'),
    path('login/', views.pagina_login, name='login'),
    path('cadastro_professor/', views.pagina_cadastrop, name='cadastrop'),
    path('cadastro_gerstao/', views.pagina_cadastrog, name='cadastrog'),
    path('salas/', views.pagina_salas, name='salas'),
    path('monitoramento/', views.pagina_monitoramento, name='monitoramento'),
    path('presenca/', views.pagina_presenca, name='presenca'),
    path('musica/', views.pagina_musica, name='musica'),
    path('autoavaliacao/', views.pagina_autoavaliacao, name='autoavaliacao'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)