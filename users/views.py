from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from .forms import RegistroForm, LoginForm
from .models import Usuario
from django.urls import reverse_lazy
from django.contrib.auth import logout

def minha_view_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("Recebido um POST")
        if form.is_valid():
            print("Formulário é válido")

            # Autentica o usuário
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('../')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logoutUsuario(request):
    logout(request)
    return redirect('../')

class RegistrarUsuario(View):
    template_name = 'registrar.html'

    def get(self, request):
        # Cria uma instância do formulário de registro sem dados do POST
        form = RegistroForm()  # Remova o request.POST daqui
        print(form)
        # Renderiza o template 'registrar.html' com o formulário
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # Cria uma instância do formulário de registro com os dados do POST
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Realiza qualquer lógica adicional de validação aqui
            # ...

            # Salva o novo usuário no banco de dados
            novo_usuario = form.save()

            # Redireciona para a página de login ou outra página desejada
            return redirect('login')

        # Se o formulário não for válido, renderiza o template 'registrar.html' com o formulário e os erros
        return render(request, self.template_name, {'form': form})
