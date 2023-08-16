from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome, name='welcome'),
    path('upload/', views.upload, name='upload'),
    path('download/<str:file_name>/', views.download_csv, name='download_csv')
]
