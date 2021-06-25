from django.urls import path

from import_file import views

urlpatterns = [
    path('', views.importar, name="Importar"),
]
