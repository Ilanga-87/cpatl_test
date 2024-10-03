from django.urls import path
from .views import get_employees, load_employees

urlpatterns = [
    path("", get_employees, name='get_employees'),
    path('load-employees/<int:id>/', load_employees, name='load_employees'),
]