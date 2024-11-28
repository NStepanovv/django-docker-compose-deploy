from django.urls import path
from . import views

urlpatterns = [
    path('video/<int:week_number>/', views.get_video, name='get_video'),
    path('video/last/', views.get_last_available_video, name='get_last_video'),
]