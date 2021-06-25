"""challenge_back URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from .router import router

from import_file import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.importar, name="Importar"),
    path('api/', include(router.urls)),
]
