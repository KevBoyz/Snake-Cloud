from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.userpage, name='userpage'),
    path('', views.users_list, name='userslist')
]
