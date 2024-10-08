from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from .forms import RegistroForm, LoginForm
from .models import Usuario
from django.contrib.auth import logout

def minha_view_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('persona:persona_create')
            else:
                # Adicione uma mensagem de erro se a autenticação falhar
                form.add_error(None, 'Usuário ou senha incorretos')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


def logoutUsuario(request):
    logout(request)
    return redirect('../')
class RegistrarUsuario(View):
    template_name = 'register.html'

    def get(self, request):
        form = RegistroForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            novo_usuario = form.save()
            return redirect('users:login')  # Redireciona para login
        else:
            # Exibe os erros no template
            return render(request, 'user/register.html', {'form': form, 'errors': form.errors})
