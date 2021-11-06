from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # View de login
    # path('login/', views.user_login, name='login'),
    path('', views.dashboard, name='dashboard'),

    # url para fazer o login na aplicação
    path('login/', auth_views.LoginView.as_view(), name='login'),

    # url para fazer o logout da aplicação
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # url para alteração de senha
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),

    # url que confirma a alteração de senha
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]