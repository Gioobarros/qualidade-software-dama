from django.views import View
from django.urls import reverse
from .models import Relato
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
    template_name = 'relato.html'

    def get(self, request, *args, **kwargs):
        relatos = Relato.objects.all().order_by('-created_at')
        return render(request, self.template_name, {'relatos': relatos})

    def post(self, request, *args, **kwargs):
        text = request.POST.get('text')
        if text:
            relato = Relato(Relato=text)
            relato.save()
            return redirect('dama:relato')
        return render(request, self.template_name, {})