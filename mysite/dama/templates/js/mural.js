document.addEventListener('click', function(event){

})

function verRelato(){
    var teste = document.createElement('div')
    
}

function mostraModal(relato) {
    var coluna = relato.dataset.column;
    var modal = document.getElementById('relato-modal');
    modal.classList.remove('oculto');
    modal.className = `janela-modal coluna-${coluna}`;
    
    var main = document.getElementById('main');
    main.classList.add('embassado');
}

document.addEventListener('click', function(event) {
    var main = document.getElementById('main')
    var modal = document.getElementById('relato-modal')

    // se o click aconteceu fora do modal, oculta ele
    if(main.classList.contains('embassado') && !modal.contains(event.target)){
        main.classList.remove('embassado')
        var modal = document.getElementById('relato-modal')
        modal.classList.remove('janela-modal')
        modal.classList.add('oculto')
    }
    else{ 
        // checa se é pra abrir o modal
        if(event.target.closest('td'))
            mostraModal(event.target.closest('td'))
    
        else if (event.target.id == 'home')
            window.location.href = "index.html"
    
        else if (event.target.id == 'denunciar')
            window.location.href = "denuncia.html"
    
        else if (event.target.id == 'header-login')
            window.location.href = "login.html"
    
        else if (event.target.id == 'header-conta')
            window.location.href = "cadastro.html"
    }

});

function novoComentario(){
    var nome_usuario = document.createElement('p')
    nome_usuario.textContent = "anonimo12345"

    var imagem_usuario = document.createElement('img')
    imagem_usuario.src = "../images/profile.png"
    imagem_usuario.alt = "icone de usuario"

    var div_usuario = document.createElement('div')
    div_usuario.classList.add('usuario-id')
    div_usuario.classList.add('borda1')
    div_usuario.appendChild(imagem_usuario)
    div_usuario.appendChild(nome_usuario)

    var texto_comentario = document.createElement('p')
    var conteudo_comentario = document.getElementById('comentario-input')
    texto_comentario.textContent = conteudo_comentario.value
    conteudo_comentario.value = ''

    var div_texto = document.createElement('div')
    div_texto.classList.add('relato-texto')
    div_texto.appendChild(texto_comentario)

    var secao = document.createElement('section')
    secao.appendChild(div_usuario)
    secao.appendChild(div_texto)

    var comentario = document.createElement('div')
    comentario.classList.add('borda2')
    comentario.classList.add('comentario')
    comentario.appendChild(secao)

    var comentarios = document.getElementById('comentarios')
    comentarios.append(comentario)
    
}


