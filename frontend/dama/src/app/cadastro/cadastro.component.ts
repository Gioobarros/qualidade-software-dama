import { Component } from '@angular/core';
import { ProfissionalService, Profissional } from '../services/profissional.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-cadastro',
  standalone: true,
  imports: [FormsModule],
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

  senhaRepetida: string = '';

  constructor(private profissionalService: ProfissionalService) { }

  onSubmit() {
    if (! (this.profissional.senha.length >= 8 && /\d/.test(this.profissional.senha) && /[A-Za-z]/.test(this.profissional.senha))) {
      alert('A senha deve ter no mínimo 8 caracteres, incluindo letras e números.');
      return;
    }

    if (! (this.profissional.senha === this.senhaRepetida)) {
      alert('As senhas não coincidem. Verifique os campos de senha.');
      return;
    }

    this.profissionalService.registerProfissional(this.profissional).subscribe(response => {
      console.log('Profissional cadastrado:', response);
      this.resetForm();
    }, error => {
      console.error('Erro ao cadastrar profissional:', error);
    });
  }

  resetForm() {
    this.profissional = {
      nome_completo: '',
      cpf: '',
      login: '',
      senha: '',
      conselho: '',
      contato: '',
      email: '',
      bio: ''
    };
    this.senhaRepetida = '';
  }
}
