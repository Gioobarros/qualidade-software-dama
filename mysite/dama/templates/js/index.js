
document.addEventListener('click', function(event){

    if (event.target.id === 'denuncia-banner')
        var janela = 'denuncia.html'
    else if (event.target.id === 'header-login')
        var janela = 'login.html'
    else if (event.target.id === 'header-conta')
        var janela = 'cadastro.html'

    window.location.href = janela
})