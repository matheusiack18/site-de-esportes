from django import forms
from.models import Pedido_order, Cliente
from django.contrib.auth.models import User
from django import forms
from django.core.mail import send_mail
from lojaproject import settings
# from setings impot EMAIL_FALE_CONOSCO

class Checar_PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido_order
        fields = ["ordernando_por","endereco_envio","telefone","email", "pagamento_method"]

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
    

class ClienteEntrarForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

# class FaleConoscoForm(forms.Form):
#     Nome = forms.CharField(label = "Digite seu Nome")
#     email = forms.EmailField(label = "Digite seu email")
#     mensagem = forms.CharField(required=True, widget=forms.Textarea)


class FaleConoscoForm(forms.Form):
    nome = forms.CharField(required=True, label='Informe seu Nome')
    email_origem = forms.EmailField(label ='Informe seu email')
    mensagem = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows':5}))
    
    def enviar_mensagem_por_email(self):
        send_mail('FALE CONOSCO: Mensagem recebida.',
        self.data['mensagem'],
        self.data['email_origem'],
        ['settings.EMAIL_FALE_CONOSCO'],
        fail_silently=False)