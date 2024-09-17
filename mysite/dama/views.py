import re
from .models import *
from django.views import View
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class CadastroView(View):
    def get(self, request,*args, **kwargs):
        return render(request, "cadastro.html")
    
    def post(self, request, *args, **kwargs):
        dados_requisicao = request.POST

        if 'nome_login' in dados_requisicao and 'senha' in dados_requisicao:
            nome_login = dados_requisicao.get('nome_login')

            senha = dados_requisicao.get('senha')

            # se for profissional
            if 'crp' in dados_requisicao and 'nome_completo' in dados_requisicao:
                nome_completo = dados_requisicao.get('nome_completo')

                crp = dados_requisicao.get('crp')

                email = dados_requisicao.get('email')


                contato = dados_requisicao.get('contato')

                validacao_contato = re.search(r'^\d{2}\s*\d{9}$', contato)

                # se o contato não foi validado
                if validacao_contato is None:
                    return render(request, "cadastro.html", context={'erro': 'contato invalido'})

                else:

                    usuario = User.objects.create_user(
                        username=nome_login,
                        password=senha,
                        email=email
                    )

                    novo_usuario = UsuarioProfissional.objects.create(
                        nome_login=nome_login,
                        senha=senha,
                        nome_completo=nome_completo,
                        cadastro_crp=crp,
                        email=email,
                        telefone=contato,
                        usuario = usuario,
                    )

                    novo_usuario.save()
                
            # se for ong
            if 'cnpj' in dados_requisicao and 'razao_social' in dados_requisicao:
                razao_social = dados_requisicao.get('razao_social')

                cnpj = dados_requisicao.get('cnpj')

                email = dados_requisicao.get('email')

                contato = dados_requisicao.get('contato')

                validacao_contato = re.search(r'^\d{2}\s*\d{9}$', contato)

                # se o contato não foi validado
                if validacao_contato is None:
                    return render(request, "cadastro.html", context={'erro': 'contato invalido'})

                else:
                    usuario = User.objects.create_user(
                        username=nome_login,
                        password=senha,
                        email=email
                    )

                    novo_usuario = UsuarioOng.objects.create(
                        nome_login=nome_login,
                        senha=senha,
                        razao_social=razao_social,
                        cnpj=cnpj,
                        email=email,
                        telefone=contato,
                        usuario = usuario,
                    )

                    novo_usuario.save()
                

            # se for anonimo
            else:        
                usuario = User.objects.create_user(
                        username=nome_login,
                        password=senha,
                )     

                novo_usuario = UsuarioAnonimo.objects.create(
                        nome_login=nome_login,
                        senha=senha,
                        usuario = usuario,
                    )

                novo_usuario.save()
                
            return redirect(reverse('dama:index'))

        else:
            return render(request, 'cadastro.html', context={'erro': 'preencha o login e senha'})


class LogarView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        dados_requisicao = request.POST

        if 'nome_login' in dados_requisicao and 'senha_usuario' in dados_requisicao:
            nome_login = dados_requisicao.get('nome_login')
            senha = dados_requisicao.get('senha_usuario')

            usuario = authenticate(username=nome_login, password=senha)

            if usuario is not None:
                login(request, usuario)
                next_url = request.POST.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect(reverse('dama:index'))
            else:
                return render(request, 'login.html', {'erro': 'Nome de usuário ou senha incorretos.'})
        else:
            return render(request, 'login.html', {'erro': 'Por favor, preencha todos os campos.'})


class LogoutView(View):
        def post(self, request, *args, **kwargs):
            logout(request)
            return HttpResponseRedirect(reverse('dama:index'))
        

class EditarPerfilView(View):
    def get(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
            usuario = request.user 

            contexto = {}

            if hasattr(usuario, 'usuarioanonimo'):

                contexto['tipo_usuario'] = 'anonimo'

            elif hasattr(usuario, 'usuarioprofissional'):

                contexto['tipo_usuario'] = 'profissional'
            
            elif hasattr(usuario, 'usuarioong'):

                contexto['tipo_usuario'] = 'ong'
            
            else:

                contexto['tipo_usuario'] = 'problema_usuario'

            return render(request, "editar.html", context=contexto)
        

        return render(request, "crud.html")

    def post(self, request, *args, **kwargs):

        if request.user.is_authenticated:

            contexto = {}

            usuario_logado = request.user 

            dados_requisicao = request.POST

            if 'nome_login' in dados_requisicao and 'senhaa' in dados_requisicao:

                nome_login = dados_requisicao.get('nome_login')

                senha = dados_requisicao.get('senhaa')

                if hasattr(usuario_logado, 'usuarioanonimo'):

                    usuario = UsuarioAnonimo.objects.get(usuario=usuario_logado)

                    if usuario is not None:
                        
                        usuario.nome_login = nome_login

                        usuario.senha = senha
                        
                        usuario.save()

                        usuario.usuario.username = nome_login

                        usuario.usuario.email = email

                        usuario.usuario.set_password(senha) 

                        usuario.usuario.save()

                        update_session_auth_hash(request, usuario.usuario)

                        return HttpResponseRedirect(reverse('dama:perfil'))

                    else:
                        contexto = {
                            'mensagem': 'usuario não foi encontrado no banco'
                        }
                    

                elif hasattr(usuario_logado, 'usuarioprofissional'):

                    usuario = UsuarioProfissional.objects.get(usuario=usuario_logado)

                    if usuario is not None:

                        if 'crp' in dados_requisicao and 'nome_completo' in dados_requisicao:

                            nome_completo = dados_requisicao.get('nome_completo')

                            crp = dados_requisicao.get('crp')

                            email = dados_requisicao.get('email')

                            contato = dados_requisicao.get('contato')

                            validacao_contato = re.search(r'^\d{2}\s*\d{9}$', contato)

                            usuario.nome_login = nome_login

                            usuario.senha = senha

                            usuario.nome_completo = nome_completo

                            usuario.cadastro_crp = crp

                            usuario.email = email

                            usuario.telefone = contato

                            usuario.save()

                            usuario.usuario.username = nome_login

                            usuario.usuario.email = email

                            usuario.usuario.set_password(senha) 

                            usuario.usuario.save()

                            update_session_auth_hash(request, usuario.usuario)

                            return HttpResponseRedirect(reverse('dama:perfil'))
                        
                    else:
                        contexto = {
                            'mensagem_erro': 'usuario não foi encontrado no banco'
                        }

                
                elif hasattr(usuario_logado, 'usuarioong'):

                    usuario = UsuarioOng.objects.get(usuario=usuario_logado)

                    if usuario is not None:

                        if 'cnpj' in dados_requisicao and 'razao_social' in dados_requisicao:

                            razao_social = dados_requisicao.get('razao_social')

                            cnpj = dados_requisicao.get('cnpj')

                            email = dados_requisicao.get('email')

                            contato = dados_requisicao.get('contato')

                            validacao_contato = re.search(r'^\d{2}\s*\d{9}$', contato)

                            usuario.nome_login = nome_login

                            usuario.senha = senha
                            
                            usuario.razao_social = razao_social

                            usuario.cnpj = cnpj

                            usuario.email = email

                            usuario.telefone = validacao_contato

                            usuario.save()

                            usuario.usuario.username = nome_login

                            usuario.usuario.set_password(senha) 

                            usuario.usuario.save()

                            update_session_auth_hash(request, usuario.usuario)

                            return HttpResponseRedirect(reverse('dama:perfil'))
                        
                    else:
                        contexto = {
                            'mensagem_erro': 'usuario não foi encontrado no banco'
                        }

                else:
                    contexto = {
                            'mensagem_erro': 'tipo de usuario não identificado'
                        }
            else:
                contexto = {
                    'mensagem_erro': 'dados obrigatorios não foram passados'
                    }
        
            return render(request, "editar.html", context=contexto) #usar o contexto para alterar
        
        else: #usuario nao autenticado
            contexto = {
                    'mensagem_erro': 'ususario não foi autenticado'
                }
            return render(request, "crud.html", context=contexto)
            
        
class DeletePerfilView(View):
        def get(self, request, *args, **kwargs):

            if request.user.is_authenticated:

                usuario_nome = request.user.username

                usuario_removido = User.objects.get(username=usuario_nome)

                usuario_removido.delete()

                return HttpResponseRedirect(reverse('dama:index'))
            
            else:
                contexto ={
                    'erro': 'problema ao autenticar usuario'
                }

                return render(request, "crud.html", context=contexto)


class PerfilView(View):
    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            try:

                usuario_perfil = request.user

                contexto = {}

                if hasattr(usuario_perfil, 'usuarioanonimo'):
                    usuario_anonimo = usuario_perfil.usuarioanonimo

                    contexto['tipo_usuario'] = 'anonimo'

                    contexto['nome_login'] = usuario_perfil.username

                    contexto['senha'] = usuario_anonimo.senha
                
                elif hasattr(usuario_perfil, 'usuarioprofissional'):
                    usuario_pro = usuario_perfil.usuarioprofissional

                    contexto['tipo_usuario'] = 'profissional'

                    contexto['nome_completo'] = usuario_pro.nome_completo

                    contexto['nome_login'] = usuario_perfil.username

                    contexto['cadastro_crp'] = usuario_pro.cadastro_crp

                    contexto['telefone'] = usuario_pro.telefone

                    contexto['email'] = usuario_pro.email

                elif hasattr(usuario_perfil, 'usuarioong'):
                    usuario_ong = usuario_perfil.usuarioong

                    contexto['tipo_usuario'] = 'ong'

                    contexto['nome_login'] = usuario_perfil.username

                    contexto['razao_social'] = usuario_ong.razao_social

                    contexto['cnpj'] = usuario_ong.cnpj

                    contexto['telefone'] = usuario_ong.telefone

                    contexto['email'] = usuario_ong.email

                else:
                    return redirect('dama:index')
            
            except Exception as e:
                contexto['mensagem_erro'] = 'erro ao carregar o usuario'

            return render(request, 'crud.html', context=contexto)
        
        else:
            return redirect('dama:login')

                
    def post(self, request, *args, **kwargs):
       pass


class CrudView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "crud.html")
    

class DenunciaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "denuncia.html")
    
    def post(self, request, *args, **kwargs):
        campos_formulario = request.POST          
        
        if not campos_formulario['descricao'] or  campos_formulario['descricao'] == '':
            return render(request, 'denuncia.html')
        
        relacao_autor = campos_formulario.get('relacao')

        descricao = campos_formulario.get('descricao')
        
        local = campos_formulario.get('locall')

        zona_cidade = campos_formulario.get('zona-cidade')

        tipo_vitima = campos_formulario.get('tipo-vitima')

        idade = campos_formulario.get('idade-vitima')

        if idade != '' and isinstance(idade, str) and idade.isdigit(): # validando idade
                idade = int(idade)
        else: 
            idade = None


        denuncia = Denuncia.objects.create(
            descricao_denuncia = descricao,
            idade_vitima = idade,
            tipo_local = local,
            relacao_autor = relacao_autor,
            zona_cidade = zona_cidade,
            vitima_tipo = tipo_vitima,
        )

        denuncia.save()

        return HttpResponseRedirect(reverse('dama:index'))



class MuralView(View):
    template_name ='mural.html'
    def get(self, request, *args, **kwargs):
        relatos = Relato.objects.all().order_by('-created_at')
        return render(request, self.template_name, {'relatos': relatos})

    
@method_decorator(login_required, name='dispatch') 
class RelatoView(View):

    template_name = 'relato.html'

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        if request.user.is_authenticated:

            usuario = request.user

            if 'text' in request.POST:

                text = request.POST.get('text')

                relato = Relato(
                    Relato=text,
                    usuario=usuario
                    )

                relato.save()

                return HttpResponseRedirect(reverse('dama:mural'))
            
            return render(request, self.template_name)
        
        return render(request, self.template_name)

class CadastroMaterialView(View):
        
        def get(self, request, *args, **kwargs):
            return render(request, "cadastromaterial.html")
                   
        def post(self, request, *args, **kwargs):
            conteudo = request.POST.get("conteudo")
            arquivo = request.FILES.get("anexo")

            if not conteudo:
                return render(request, "cadastromaterial.html", {"error": "O conteúdo é obrigatório."})
            
            #MUDAR quando usarmos User do Django na sessão!!!!!!!!
            #usuarioteste = User.objects.get(pk=2)

            material = Material(
                conteudo = conteudo,
                arquivo_anexo = arquivo,
                usuario_id = request.user.id
            )

            material.save()

            try:
                return redirect(reverse(f"dama:materiais/{material.pk}"))
            except:
                return redirect(reverse("dama:materiais"))

def MaterialDetailView(request, id):
    material = get_object_or_404(Material, id=id)
    context = {
        'material': material
    }
    return render(request, 'material_detail.html', context)


class MateriaisView(View):
    def get(self,request):
        materiais = Material.objects.all().order_by('-data_publicacao')
        return render(request, "materiais.html", {"materiais":materiais})