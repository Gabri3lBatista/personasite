from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from .forms import RegistroForm, LoginForm
from .models import Usuario
from django.contrib.auth import logout
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse


def minha_view_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({'success': True, 'message': 'Login realizado com sucesso!'})
            else:
                return JsonResponse({'success': False, 'message': 'Nome de usuário ou senha incorretos.'})
        else:
            return JsonResponse({'success': False, 'message': 'Por favor, corrija os erros no formulário.'})
    else:
        form = LoginForm()
    
    # Se não for um POST, renderiza o template com o formulário
    return render(request, 'user/login.html', {'form': form})


def logoutUsuario(request):
    logout(request)  # Desconecta o usuário
    return redirect('users:login')  # Redireciona para a URL de login
    
    
class RegistrarUsuario(View):
    template_name = 'user/register.html'

    def get(self, request):
        form = RegistroForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            novo_usuario = form.save()
            return JsonResponse({'success': True, 'message': 'Registro realizado com sucesso!'})
        else:
            # Retorna os erros como JSON
            return JsonResponse({
                'success': False,
                'message': 'Por favor, corrija os erros no formulário.',
                'errors': form.errors
            })