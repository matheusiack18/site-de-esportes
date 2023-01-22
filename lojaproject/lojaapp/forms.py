from django import forms
from.models import Pedido_order, Cliente
from django.contrib.auth.models import User


class Checar_PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido_order
        fields = ["ordernando_por","endereco_envio","telefone","email"]

class ClienteRegistrarForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())
    class Meta:
        model = Cliente
        fields = ["username","password","email","nome_completo","endereco"]

    def clean_username(self):
        unome = self.cleaned_data.get("username")
        if User.objects.filter(username=unome).exists():
            raise forms.ValidationError("ESTE CLIENTE JA EXISTE!")
        return unome