from django.urls import path
from . import views

urlpatterns = [
   # path('', views.dashboard, name='dashboard'),
   path('./', views.dashboard, name='dashboard.urls'),
]
