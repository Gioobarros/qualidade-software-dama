from django.views import View
from django.urls import reverse
from .models import Denuncia, Relato
from .forms import *
from django.shortcuts import render, HttpResponseRedirect, redirect

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class CadastroView(View):

    def get(self, request, *args, **kwargs):
        form = Teste()
        return render(request, "cadastro.html", {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = Teste(request.POST)

        if form.is_valid():  
            return HttpResponseRedirect(reverse("dama:index"))
         
        return render(request, "cadastro.html", {'form': form})

class DenunciaView(View):

    def get(self, request, *args, **kwargs):
        form = DenunciaForm()

        return render(request, "denuncia.html", {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = Teste(request.POST)
        
        if form.is_valid():  
            denuncia = form.save(commit=False)

            denuncia.save()

            return HttpResponseRedirect(reverse("dama:index"))
        
        else: 
            return render(request, "denuncia.html", {'form': form})
        
class MuralView(View):

    def get(self, request, *args, **kwargs):

        # instancia form

        return render(request, "mural.html", {'form': "passa o form "})
    
    def post(self, request, *args, **kwargs):
        form =  'instancia form'

        if form.is_valid():  
            'valida o form se preciso '

            # instancia_de_modelo = form.save(commit=False)

           #  instancia_de_modelo.save()

            return HttpResponseRedirect(reverse("dama:pagina"))
        
        else: 
            return render(request, "mural.html", {'form': "passa o form "})
        
class RelatoView(View):

    def get(self, request, *args, **kwargs):

        form = RelatoForm()

        return render(request, "relato.html", {'form': form})
    
    def post(self, request, *args, **kwargs):
        form =  RelatoForm(request.POST)

        if form.is_valid():  
            relato = form.save(commit=False)

            relato.save()

            return HttpResponseRedirect(reverse("dama:mural"))
        
        else: 
            return render(request, "mural.html", {'form': form})
        
        