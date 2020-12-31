from django.urls import path

from . import views


urlpatterns = [

  # НАШ HTML
  # URL привязки http://127.0.0.1:8000/
  path('', views.index, name = 'index'),

  path('user', views.user)
  
]