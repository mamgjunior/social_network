from django.urls import path
from . import views


urlpatterns = [
    # View de login
    path('login/', views.user_login, name='login'),
]