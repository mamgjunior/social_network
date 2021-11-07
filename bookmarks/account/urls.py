from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # View de login
    # path('login/', views.user_login, name='login'),
    path('', views.dashboard, name='dashboard'),

    # Este padrão de urls substitui todos os colocados abaixo
    path('', include('django.contrib.auth.urls')),

    # Esta url é para a criação de novos usuários
    path('register/', views.register, name='register'),

    path('edit/', views.edit, name='edit'),
]

"""
    # urls para fazer o login e logout na aplicação
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # urls para alteração de senha e confirmação da alteração
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # urls para reiniciar senhas
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
"""