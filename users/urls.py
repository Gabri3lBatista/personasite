from django.urls import path
from .views import RegistrarUsuario, minha_view_login, logoutUsuario

app_name = 'users'

urlpatterns = [
    path('registrar/', RegistrarUsuario.as_view(), name='register'),
    path('login/', minha_view_login, name='login'),
    path('logout/', logoutUsuario, name='logout'),
]