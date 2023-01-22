from django import forms
from django.db.models import fields
from.models import Pedido_order, Cliente
from django.forms import ModelForm, TextInput, EmailInput

class Checar_PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido_order
        fields = ["ordernando_por","endereco_envio","telefone","email"]
        widgets = {
            'ordernando_por': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Pedido Por'
                }),
            
                'endereco_envio': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Endereço de envio'
                }),
                'telefone': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Telefone'
                }),
                'email': EmailInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
                
        }

class ClienteRegistrarForm(forms.ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario','class': 'form-control','style': 'width: 300px;display:flex;'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Sua Senha','class': 'form-control','style': 'width: 300px;display:flex;'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Seu Email','class': 'form-control','style': 'width: 300px;display:flex;'}))
    class Meta:
        model = Cliente
        fields = ["usuario","senha","email","nome_completo","endereco"]
        widgets = {
                'nome_completo': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Nome Completo'
                }),
                'endereco': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Endereço'
                }),
                
        }