from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('<str:room>', views.room_view),
]
