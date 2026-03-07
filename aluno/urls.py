
from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, update, delete, salvar_nota, deletar_nota


urlpatterns = [
    path('', home, name="home"),
    path('salvar/', salvar,name="salvar"),
    path('editar/<int:id>', editar,name="editar"),
    path('update/<int:id>', update,name="update"),
    path('delete/<int:id>', delete,name="delete"),
    path('salvar-nota/<int:id>', salvar_nota, name="salvar_nota"),
    path('delete-nota/<int:id>', deletar_nota, name="delete_nota"),
    
]
