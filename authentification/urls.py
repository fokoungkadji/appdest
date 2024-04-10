from django.urls import path
from . import views


app_name = 'authentification'

urlpatterns =[
    path('index', views.index, name='index'),
    path('connection', views.connection, name='connection'),
    path('creecompte', views.creecompte, name='creecompte'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
]