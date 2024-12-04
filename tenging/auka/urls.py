from django.contrib import admin
from django.urls import path, include  # include is required to link app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dataapp.urls')),  # Link dataapp URLs here
]
