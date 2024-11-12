import { Component } from '@angular/core';
import { ProfissionalService, Profissional } from '../services/profissional.service';
import { FormsModule } from '@angular/forms'; // Importar FormsModule

@Component({
  selector: 'app-cadastro',
  standalone: true,
  imports: [FormsModule], // Adicione FormsModule aqui
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css']
})
export class CadastroComponent {
  profissional: Profissional = {
    nome_completo: '',
    cpf: '',
    login: '',
    senha: '',
    conselho: '',
    contato: '',
    email: '',
    bio: ''
  };

  constructor(private profissionalService: ProfissionalService) { }

  onSubmit() {
    this.profissionalService.registerProfissional(this.profissional).subscribe(response => {
      console.log('Profissional cadastrado:', response);
      // Aqui você pode adicionar lógica para redirecionar ou mostrar uma mensagem de sucesso
    }, error => {
      console.error('Erro ao cadastrar profissional:', error);
    });
  }
}