from django.forms import ModelForm
from RenderApp.models import Fornecedor,Empresa,Interesse,Newsletter

class FormFornecedor(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome_completo','email','telefone','endereco','cidade','residuos','tipo_residuos','volume_produto','image']
    
class FormEmpresa(ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome_empresa','cnpj','endereco','email','telefone']

class FormInteresse(ModelForm):
    class Meta:
        model = Interesse
        fields = ['nome_empresa','email']

class FormNewsletter(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']