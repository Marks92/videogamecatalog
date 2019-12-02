from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('unsubscribe/<int:id>', views.delete_user, name='delete'),
    path('games/', views.view_games, name='games'),
    path('update/<int:id>', views.update_user, name='update'),
    path('users/', views.view_users, name='users'),
    path('logout/', views.logout, name='logout'),
]