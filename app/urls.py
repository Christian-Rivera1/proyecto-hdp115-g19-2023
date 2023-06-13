from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index
from app import views

app_name = 'app'

urlpatterns = [
    path('index/',index, name='index'),
    path('discapacidad/', views.discapacidad, name='discapacidad'),
    path('empresas/', views.empresas, name='empresas'),
    path('login/', views.login, name='login'),
    #path('login/', views.login, name='login'),
    path('tabla/',views.tabla, name='tabla'),
    path('editarest/', views.editarestadisticas, name='editest'),
    path('edit/', views.editando, name = 'edit'),
    path('save_data', views.save_data, name= 'save_data'),
    path('logout/', views.exit, name= 'exit')
    
    

]
