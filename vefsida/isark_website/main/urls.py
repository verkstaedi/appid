from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('hafa-samband/', views.contact, name='contact'),
    path('accounts/', include('allauth.urls')),
]
