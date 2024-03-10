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
    return render(request, 'user/login.html', {'form': form})

def logoutUsuario(request):
    logout(request)
    return redirect('../')

class RegistrarUsuario(View):
    template_name = 'register.html'
    
    def get(self, request):
        # Cria uma instância do formulário de registro sem dados do POST
        form = RegistroForm()  # Remova o request.POST daqui
        # Renderiza o template 'registrar.html' com o formulário
        return render(request, 'user/register.html', {'form': form})
    def post(self, request):
        # Cria uma instância do formulário de registro com os dados do POST
        form = RegistroForm(request.POST)
        print('xxxx')
        if form.is_valid():
            # Realiza qualquer lógica adicional de validação aqui
            # ...

            # Salva o novo usuário no banco de dados
            novo_usuario = form.save()
            print('entrou')
            # Redireciona para a página de login ou outra página desejada
            return redirect('users:login')  # Ajuste aqui para o nome correto da URL de login
        else:
            # Exibe mensagens de erro no console para ajudar na depuração
            print(form.errors)

        # Se o formulário não for válido, renderiza o template 'registrar.html' com o formulário e os erros
        return render(request, 'user/register.html', {'form': form, 'errors': form.errors})
