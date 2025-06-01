from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('consultation-request/', views.consultation_request, name='consultation_request'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('test-logs/', views.test_logging)

]