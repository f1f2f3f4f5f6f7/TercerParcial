"""
URL configuration for djangologin project.

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
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('notas/', views.notas, name='notas'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('addNotas/', views.addNotas, name='addNotas'),
    path('eliminacionNota/<int:nota_id>/', views.eliminacionNota, name='eliminacionNota'),
    path('editarNota/<int:nota_id>/', views.editarNota ,name ='editarNota' ),
    path('getNota/<int:nota_id>/', views.getNota, name='getNota'),
]
