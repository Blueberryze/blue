from urllib import request

from django.shortcuts import render, redirect
from .models import Item

def listar_itens(request):
    itens = Item.objects.all()
    return render(request, 'listar_itens.html', {'itens': itens})

def cadastrar_produtos(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        qtd =int(request.POST.get('qtd'))
        preco = float(request.POST.get('preco'))
        Item.objects.create(
            nome=nome,
            descricao=descricao,
            qtd=qtd,
            preco=preco,
        
        )

        return redirect("listar_itens")
    return render(request, 'cadastrar_produtos.html')

