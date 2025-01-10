from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_list, name='api_list'),
    path('create/', views.api_create, name='api_create'),
    path('update/<int:pk>/', views.api_update, name='api_update'),
    path('delete/<int:pk>/', views.api_delete, name='api_delete'),
]
