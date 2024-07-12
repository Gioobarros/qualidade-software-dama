
document.addEventListener('click', function(event){
    if (event.target.id === 'denuncia-banner')
        window.location.href = 'denuncia.html'
    else if (event.target.id === 'header-login')
        window.location.href = 'login.html'
    else if (event.target.id === 'header-conta')
        window.location.href = 'cadastro.html'
    else if (event.target.id === 'mural')
        window.location.href = 'mural.html'
    else if (event.target.id === 'logo-img')
        window.location.href = 'index.html'
})