document.addEventListener('click', function(event){
    if (event.target.id == 'home')
        window.location.href = "index.html"
    else if (event.target.id == 'denunciar')
        window.location.href = "denuncia.html"
    else if (event.target.id == 'header-login')
        window.location.href = "login.html"
    else if (event.target.id == 'header-conta')
        window.location.href = "cadastro.html"
})