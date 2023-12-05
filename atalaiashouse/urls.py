from django.urls import path
from atalaiashouse import views

urlpatterns = [        
        path('', views.index, name='index'),
  
        path('', views.cadastro_novo, name='cadastro_novo'),

               ]