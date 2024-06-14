const bairrosPorZona = {
    norte: ["Bairro A", "Bairro B", "Bairro C"],
    sul: ["Bairro D", "Bairro E", "Bairro F"],
    leste: ["Bairro G", "Bairro H", "Bairro I"],
    oeste: ["Bairro J", "Bairro K", "Bairro L"]
  };

  // Dados das ruas por bairro
  const ruasPorBairro = {
    "Bairro A": ["Rua A1", "Rua A2", "Rua A3"],
    "Bairro B": ["Rua B1", "Rua B2", "Rua B3"],
    "Bairro C": ["Rua C1", "Rua C2", "Rua C3"],
    "Bairro D": ["Rua D1", "Rua D2", "Rua D3"],
    "Bairro E": ["Rua E1", "Rua E2", "Rua E3"],
    "Bairro F": ["Rua F1", "Rua F2", "Rua F3"],
    "Bairro G": ["Rua G1", "Rua G2", "Rua G3"],
    "Bairro H": ["Rua H1", "Rua H2", "Rua H3"],
    "Bairro I": ["Rua I1", "Rua I2", "Rua I3"],
    "Bairro J": ["Rua J1", "Rua J2", "Rua J3"],
    "Bairro K": ["Rua K1", "Rua K2", "Rua K3"],
    "Bairro L": ["Rua L1", "Rua L2", "Rua L3"]
  };

window.onload = mostrarBairros
  
function mostrarBairros(){
    // pega o select do form 
    const bairroSelect = document.getElementById('bairros')

    // crio um option generico
    bairroSelect.innerHTML = '<option value="">Selecione um Bairro</option>'

    for(const[zona, bairros] of Object.entries(bairrosPorZona)){
        const agrupamento_bairros = document.createElement('optgroup')

        agrupamento_bairros.label = `Zona ${zona.charAt(0).toUpperCase() + zona.slice(1)}`

        bairros.forEach(bairro =>{
            const opcao = document.createElement('option')
            opcao.value = bairro
            opcao.textContent = bairro.charAt(0).toUpperCase() + bairro .slice(1)
            agrupamento_bairros.appendChild(opcao);
        })
        bairroSelect.appendChild(agrupamento_bairros)
    }
  }

function mostrarRuas() {
    // pego o bairro selecionado
    const bairroSelecionado = document.getElementById('bairros').value;
    // pego o select da rua
    const ruaSelect = document.getElementById('rua');
  
    // Limpa as opções existentes
    ruaSelect.innerHTML = '<option value="">Selecione uma Rua</option>';
  
    // se o bairro for selecionado, e estiver presente nos registros
    if (bairroSelecionado && ruasPorBairro[bairroSelecionado]) {
      // Adiciona as novas opções
      ruasPorBairro[bairroSelecionado].forEach(rua => { // pego cada rua do bairro...
        const option = document.createElement('option');
        option.value = rua;
        option.textContent = rua;
        ruaSelect.appendChild(option); // e coloco como opção para ser selecionado
      });
    }
  }

const botaoDenunciar = document.getElementById('denunciar')


botaoDenunciar.addEventListener('click', function(event){
  event.preventDefault()

  var janela = document.getElementById('denuncia-feita')
  if(janela.classList.contains('oculto')){
    setTimeout(function(){
      if(janela.classList.contains('oculto')){
        janela.classList.remove('oculto')
        janela.classList.add('denuncia-feita')
        var main = document.getElementById('main')
        main.classList.add('embassado')
      }
    },1000)
  
    setTimeout(function(){
        janela.classList.add('oculto')
        janela.classList.remove('denuncia-feita')
        var main = document.getElementById('main');
        main.classList.remove('embassado');
        event.target.closest('form').submit()
    },8000)
  } 
  else{
      var janela = document.getElementById('denuncia-feita')
      janela.classList.remove('denuncia-feita');
      janela.classList.add('oculto');
      var main = document.getElementById('main');
      main.classList.remove('embassado');
  }


})

document.addEventListener('click', function(event) {
  // se não for na janela
  if (event.target.id !== 'denuncia-feita') { 
    if (event.target.id === 'login-header')
      window.location.href = 'login.html'
    else if (event.target.id === 'conta-header')
      window.location.href = 'cadastro.html'
    else{
      var janela = document.getElementById('denuncia-feita');
      if(!janela.classList.contains('oculto')){
        janela.classList.remove('denuncia-feita');
        janela.classList.add('oculto');
        var main = document.getElementById('main');
        main.classList.remove('embassado');
      }
    }
  } 
});


function login(){
  window.location.href = "login.html"
}

function criarConta(){
  window.location.href = "cadastro.html"
}