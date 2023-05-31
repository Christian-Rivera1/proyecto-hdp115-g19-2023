from django.urls import path
from .views import index
from app import views

app_name = 'app'

urlpatterns = [
    path('index/',index, name='index'),
    path('discapacidad/', views.discapacidad, name='discapacidad'),
    path('empresas/', views.empresas, name='empresas'),
    path('login/', views.login, name='login'),
    path('tabla/',views.tabla, name='tabla')
    #path("", views.index, name="index"),
    #path("graficos/grafico1", views.grafico1, name="grafico1"),
    #path("graficos/grafico2", views.grafico2, name="grafico2"),
    #path("graficos/grafico3", views.grafico3, name="grafico3")
    

]
