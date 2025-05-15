from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('work/<slug:slug>/', views.project_detail, name='project_detail'),
]