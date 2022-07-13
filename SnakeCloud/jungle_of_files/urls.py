from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload, name='upload'),
    path('dashboard/post/<str:id>/', views.dashboard_post, name='post'),
]
