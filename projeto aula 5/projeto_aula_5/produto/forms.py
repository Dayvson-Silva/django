from django import forms
from .models import Produto


class ContatoForm(forms.Form):
    nome  = forms.CharField(max_length=100, label='nome')
    email = forms.EmailField(label='Email')
    mensagem = forms.CharField(label ='Mensagem', widget=forms.Textarea)

class ProdutoForm(forms.Form):
    class Meta:
        model = Produto
        fields = ['nome', 'preco','estoque']
        labels = {
            'nome': 'Nome',
            'preco': 'Preco',
            'estoque': 'Estoque'
        }