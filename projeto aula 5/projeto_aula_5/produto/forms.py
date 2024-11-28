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
# VALIDAÇÃO DE ERRO 
def clean_nome(self):
    nome = self.cleaned_data.get('nome')
    if len(nome) < 3 :
        raise forms.ValidationError("errou otario tem que ter 3 palavras ")
    return nome

# ISSO É PARA COLOCAR EM BIUTAREFAS
def clean_descricao(self):
    descricao = self.cleaned_data.get('descricao')
    if descricao and len(descricao) < 10 :
        raise forms.ValidationError("errou otario tem que ter 10 palavras ")
    return descricao