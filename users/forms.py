from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    senha_confirmacao = forms.CharField(widget=forms.PasswordInput, label='Confirmar senha')

    class Meta:
        model = Usuario
        fields = ("username", "email", "password")  # Adicionar "email" se necessário
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('password')
        senha_confirmacao = cleaned_data.get('senha_confirmacao')

        if senha and senha_confirmacao and senha != senha_confirmacao:
            self.add_error('senha_confirmacao', 'As senhas não coincidem')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash de senha
        if commit:
            user.save()
        return user
    
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)