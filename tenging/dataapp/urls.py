from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),  # URL for creating a new Notendur
]
