from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('question/', views.details, name = 'details'),
    path('results/', views.results, name = 'results'),
]