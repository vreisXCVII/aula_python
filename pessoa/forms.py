from django import forms
from .models import PessoaModel
from django.contrib.admin import widgets
from pessoa.models import ContatoModel

class PessoaForm(forms.ModelForm):
    
    cliente_nome = forms.CharField(required=True, label="Nome")
    endereco = forms.CharField(required=True, label="endereco")
    cliente_cpf = forms.CharField(required=True, label="CPF")
    cliente_rg = forms.CharField(required=True, label="Rg cliente")

    class Meta:
        model = PessoaModel
        fields = [
            'cliente_nome',
            'endereco',
            'cliente_cpf',
            'cliente_rg'
        ]
           
        
class ContatoForm(forms.ModelForm):
    
    
    venda_data = forms.CharField(required=True, label="data venda")
    valor_total_venda = forms.FloatField(required=True, label="valor total")

    
    class Meta:
        model = ContatoModel
        fields = [
            'venda_data',
            'valor_total_venda',
        ]
    widgets = {'venda_data':forms.DateInput(attrs={'class':'js-date'})}
    
    
