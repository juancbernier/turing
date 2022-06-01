from pipes import Template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from .turing import inicio

def saludo(request):
    
    if request.method == 'POST':
        auto = request.POST['automata']
        
        aux = inicio(auto);

        return render(request, "index.html", {"taux":aux})
    return render(request, "index.html")