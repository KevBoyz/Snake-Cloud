from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dash'),
    path('new/', views.new_article),
    path('articles/<str:article>', views.article),
    path('articles/delete/<str:article>', views.delete),
]
