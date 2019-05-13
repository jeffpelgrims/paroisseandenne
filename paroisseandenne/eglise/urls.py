from . import views
from django.urls import path


urlpatterns = [
    path('', views.accueil),
    path('<str:tag>/', views.detail)
]