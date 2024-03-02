from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    senha_confirmacao = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ("username", "password", 'senha_confirmacao')
        widgets = {'password': forms.PasswordInput}

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('password')
        senha_confirmacao = cleaned_data.get('senha_confirmacao')

        # Executa a validação padrão do formulário
        if senha and senha_confirmacao and senha != senha_confirmacao:
            self.add_error('senha_confirmacao', 'As senhas não coincidem')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)