from django import forms
from django.db.models import fields
from.models import Pedido_order
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
                'email': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
                
        }

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
                'email': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
                
        }


ClienteRegistrarForm    