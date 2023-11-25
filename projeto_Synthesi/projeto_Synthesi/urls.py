"""
URL configuration for projeto_Synthesi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_Synthesi import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicio, name='inicio'),
    path('cadastroProfessor/', views.pagina_cadastro_prof, name='cadastro_professor'),
    path('cadastroGestão/', views.pagina_cadastro_gest, name='cadastro_gestao'),
    path('salas/', views.pagina_salas, name='salas'),
    path('monitoramento/', views.pagina_monitoramento, name='monitoramento'),
    path('presenca/', views.pagina_presenca, name='presenca'),
    path('musica/', views.pagina_musica, name='musica'),
    path('autoavaliacao/', views.pagina_autoavaliacao, name='autoavaliacao'),    
]