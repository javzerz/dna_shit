from django.urls import path
from . import views
from upload_dna.models import Data
from django.views.generic import ListView, DetailView

app_name = 'upload'

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('', views.home, name='home'),
    path('upload/add/', views.DataCreate.as_view(), name='data_add'),
    path('upload/detail/', views.detail, name='detail'),
    path('register/', views.UserFormView.as_view(), name='register'),
]
