
from django.urls import path, include
from .views import cars_spec

urlpatterns = [
    path('carspec', cars_spec)
]
