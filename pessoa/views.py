from django.shortcuts import render, redirect, get_object_or_404
from .forms import PessoaForm
from .models import PessoaModel

##from django.http import HttpResponse

# Create your views here.

def list_pessoa(request):
    form = PessoaModel.objects.all() ##ler a tabela pessoa
    context = {
        'form':form,
    }
    return render(request, 'listar.html', context)

def insert_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_pessoa')
    context = {
        'form':form
    }
    return render(request, 'novo3.html',context)

def update_pessoa(request, id):
    pessoa = get_object_or_404(PessoaModel, pessoa_id=id)
    form = PessoaForm(request.POST or None, instance = pessoa)
    if form.is_valid():
        form.save()
        return redirect('list_update')
    context = {
        'form':form,
    }
    return render(request, 'novo2.html', context)

def home_pessoa(request, id):
    pessoa = get_object_or_404(PessoaModel, pessoa_id=id)
    form = PessoaForm(request.POST or None, instance = pessoa)
    if form.is_valid():
        form.save()
        return redirect('list_pessoa')
    context = {
        'form':form,
    }
    return render(request, 'novo.html', context)


def delete_pessoa(request, id):
    pessoa = get_object_or_404(PessoaModel, pessoa_id=id)
    form = PessoaForm(request.POST or None, instance = pessoa)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('list_pessoa')
    context={
        'form':form,
    }
    return render(request, 'novo2.html', context)


def view_pessoa(request, id):
    pessoa = get_object_or_404(PessoaModel, pessoa_id=id)
    form = PessoaForm(request.POST or None, instance = pessoa)
    if request.method == 'POST':
        return redirect('list_pessoa')
    context={
        'form':form,
    }
    return render(request, 'novo2.html', context)
