from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.filter_csv, name='upload'),
    path('onlynull/', views.only_null, name='onlynull'),
    path('download/<str:file_name>/', views.download_csv, name='download_csv'),]