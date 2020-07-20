from django.shortcuts import render_to_response,render,redirect
from django.contrib import messages
from api.models import *
from api.forms import *


def index(request):
    return render(request, 'index.html')

#Forma
def forma(request):
    dados = Tbforma.objects.all()
    return render(request, 'forma.html',{'dados': dados})

def forma_new(request):
    info={
        "titulo": "Cadastrar de Forma",
        "link_principal": "forma",
    }
    form = form_forma(request.POST or None)
    if request.method == 'POST':
        form = form_forma(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Forma cadastrada com sucesso.')
            return redirect(info['link_principal'])
    return render(request, 'form.html', {'info':info,'form': form})

def forma_edit(request,id):
    info = {
        "titulo": "Editar Forma",
        "link_principal": "forma",
    }
    instance = Tbforma.objects.get(cod_forma=id)
    form = form_forma(request.POST or None, instance=instance)
    if request.method == 'POST':
        form.save()
        messages.success(request, 'Forma alterada com sucesso.')
        return redirect(info['link_principal'])
    return render(request, 'form.html', {'info':info,'form': form})

def forma_delete(request,id):
    try:
        Tbforma.objects.filter(cod_forma=id).delete()
        messages.success(request, 'Forma deletada com sucesso.')
    except:
        messages.warning(request, 'Nao é possivel deletar porque esta relacionado com outro registro ')
    return redirect("forma")


#Materia
def materia(request):
    dados = Tbmateria.objects.all()
    return render(request, 'materia.html',{'dados': dados})

def materia_new(request):
    info={
        "titulo": "Cadastrar Materia",
        "link_principal": "materia",
    }
    form = form_materia(request.POST or None)
    if request.method == 'POST':
        form = form_materia(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Materia cadastrada com sucesso.')
            return redirect(info['link_principal'])
    return render(request, 'form.html', {'info':info,'form': form})

def materia_edit(request,id):
    info = {
        "titulo": "Editar Materia",
        "link_principal": "materia",
    }
    instance = Tbmateria.objects.get(cod_tipomateria=id)
    form = form_materia(request.POST or None, instance=instance)
    if request.method == 'POST':
        form.save()
        messages.success(request, 'Materia alterada com sucesso.')
        return redirect(info['link_principal'])
    return render(request, 'form.html', {'info':info,'form': form})

def materia_delete(request,id):
    try:
        Tbmateria.objects.filter(cod_tipomateria=id).delete()
        messages.success(request, 'Materia deletada com sucesso.')
    except:
        messages.warning(request, 'Nao é possivel deletar porque esta relacionado com outro registro ')
    return redirect("materia")

#Tipo Processo

def tipo_processo(request):
    dados = Tbtipoprocesso.objects.all()
    return render(request, 'tipo_processo.html',{'dados': dados})

def tipo_processo_new(request):
    info={
        "titulo": "Cadastrar Tipo Processo",
        "link_principal": "tipo_processo",
    }
    form = form_tipoprocesso(request.POST or None)
    if request.method == 'POST':
        form = form_tipoprocesso(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de processo cadastrado com sucesso.')
            return redirect(info['link_principal'])
    return render(request, 'form.html', {'info':info,'form': form})

def tipo_processo_edit(request,id):
    info = {
        "titulo": "Alterar Tipo de Processo",
        "link_principal": "tipo_processo",
    }
    instance = Tbtipoprocesso.objects.get(cod_tipoprocesso=id)
    form = form_tipoprocesso(request.POST or None, instance=instance)
    if request.method == 'POST':
        form.save()
        messages.success(request, 'Tipo de Processo alterado com sucesso.')
        return redirect(info['link_principal'])
    return render(request, 'form.html', {'info':info,'form': form})

def tipo_processo_delete(request,id):
    try:
        Tbtipoprocesso.objects.filter(cod_tipoprocesso=id).delete()
        messages.success(request, 'Tipo de processo deletado com sucesso.')
    except:
        messages.warning(request, 'Nao é possivel deletar porque está relacionado com outro registro.')
    return redirect("tipo_processo")


#Processo

def processo(request):
    dados = Tbprocesso.objects.all()
    return render(request, 'processo.html',{'dados': dados})

def processo_new(request):
    info={
        "titulo": "Cadastrar Processo",
        "link_principal": "processo",
    }
    form = form_processo(request.POST or None)
    if request.method == 'POST':
        form = form_processo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Processo cadastrado com sucesso.')
            return redirect(info['link_principal'])
    return render(request, 'form.html', {'info':info,'form': form})

def processo_edit(request,id):
    info = {
        "titulo": "Alterar Processo",
        "link_principal": "processo",
    }
    instance = Tbprocesso.objects.get(cod_processo=id)
    form = form_processo(request.POST or None,request.FILES or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Processo alterado com sucesso.')
            return redirect(info['link_principal'])
    return render(request, 'form.html', {'info':info,'form': form})

def processo_delete(request,id):
    try:
        Tbprocesso.objects.filter(cod_processo=id).delete()
        messages.success(request, 'Processo deletado com sucesso.')
    except:
        messages.warning(request, 'Nao é possivel deletar porque está relacionado com outro registro.')
    return redirect("processo")