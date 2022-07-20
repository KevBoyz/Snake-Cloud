from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('new', views.new_room),
    path('<str:room>', views.room_view),
    path('delete/<str:room>', views.delete),
]
