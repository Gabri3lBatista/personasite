from django.urls import path
from .views import RegistrarUsuario, minha_view_login, logoutUsuario

urlpatterns = [
    path('registrar/', RegistrarUsuario.as_view(), name='registrar'),
    path('login/', minha_view_login, name='login'),
    path('logout/', logoutUsuario, name='logout'),
]