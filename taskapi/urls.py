from django.urls import path
from django.conf import settings
from .views import my_view
from . import views


urlpatterns = [
    path('task/', views.my_view , name = 'view')
]