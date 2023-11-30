from django.contrib import admin
from django.urls import path
from app_Synthesi import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicio, name='inicio'),
    path('cadastro_professor/', views.pagina_cadastrop, name='cadastrop'),
    path('cadastro_gerstao/', views.pagina_cadastrog, name='cadastrog'),
    path('eu_eo_mundo/', views.pagina_eueomundo, name='eu_eo_mundo'),
    path('salas/', views.pagina_salas, name='salas'),
    path('adicionar/', views.pagina_adicionar, name='adicionar'),
    path('adicionar_materia/', views.pagina_adicionarmateria, name='adicionar_materia'),
    path('monitoramento/<str:nome>/<str:turma>/<str:idade>/', views.pagina_monitoramento, name='monitoramento'),
    path('solicitar/<str:nome>/<str:turma>/<str:idade>/', views.pagina_solicitar, name='solicitar'),
    path('reunioes/<str:nome>/<str:turma>/<str:idade>/', views.pagina_reunioes, name='reunioes'),
    path('atividades/<str:nome>/<str:turma>/<str:idade>/', views.pagina_atividades, name='atividades'),
    path('autoavaliacao/<str:nome>/<str:turma>/<str:idade>/', views.pagina_autoavaliacao, name='autoavaliacao'),    
    path('marcar_presenca/', views.pagina_presenca, name='marcar_presenca'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)