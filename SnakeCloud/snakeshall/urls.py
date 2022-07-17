from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard),
    path('new/', views.new_article),
    path('articles/<str:article>', views.article)
]
