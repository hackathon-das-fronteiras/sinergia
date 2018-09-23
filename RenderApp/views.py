from django.shortcuts import render,redirect,get_object_or_404
from RenderApp.forms import FormFornecedor,FormEmpresa,FormInteresse,FormNewsletter
from django.contrib import messages
from RenderApp.models import Fornecedor,Interesse,Apoiadores

# Create your views here.

def home(request):
    apoiadores = Apoiadores.objects.all().order_by('-date')
    forms_newsletter = FormNewsletter(request.POST or None)
    if forms_newsletter.is_valid():
        forms_newsletter.save()
        messages.success(request,'Obrigado por se inscrever ;)') 
        return redirect('home')
    return render(request,'base.html',{'apoiadores':apoiadores})

def cad_fornecedor(request):
    title = 'Cadastro Fornecedor de Resíduos'
    if request.method == 'POST':
        forms = FormFornecedor(request.POST or None,request.FILES or None)
        if forms.is_valid():
            forms.save()
            forms = FormFornecedor()
            messages.success(request, 'Registro salvo com sucesso!')
            return render(request,'cadastro_fornecedor.html',{'forms':forms,'title':title})
    else:
        forms = FormFornecedor(request.POST or None,request.FILES or None)
        return render(request,'cadastro_fornecedor.html',{'forms':forms,'title':title})

def cad_empresa(request):
    title = "Cadastre sua Empresa"
    if request.method == 'POST':
        forms = FormEmpresa(request.POST or None)
        if forms.is_valid():
            forms.save()
            forms = FormEmpresa()
            messages.success(request, 'Registro salvo com sucesso!')
            return redirect('cad_empresa')
    else:
        forms = FormEmpresa(request.POST or None)
        return render(request,'cadastro_empresa.html',{'forms':forms,'title':title})

def consulta_residuos(request):
    title = 'Consultar Resíduos'
    registros = Fornecedor.objects.all().order_by('-date')
    return render(request,'consulta_residuos.html',{'title':title,'registros':registros})

def demo_interesse(request,pk):
    residuo = get_object_or_404(Fornecedor,id=pk)
    if request.method == 'POST':
        interesse = Interesse()
        interesse.nome_empresa = request.POST.get('nome_empresa')
        interesse.email = request.POST.get('email')
        interesse.fornecedor = residuo
        interesse.save()
        messages.success(request, 'O seu interesse foi registrado com sucesso, aguerde nosso contato!')
        return redirect('consulta_residuos')
    else:
        return render(request,'demo_interesse.html',{'residuo':residuo})