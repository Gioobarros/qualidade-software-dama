import { Component } from '@angular/core';
import { ProfissionalService, Profissional } from '../services/profissional.service';
import { FormsModule } from '@angular/forms'; // Importar FormsModule
import { HeaderComponent } from '../components/header/header.component';


@Component({
  selector: 'app-cadastro',
  standalone: true,
  imports: [FormsModule, HeaderComponent], // Adicione FormsModule aqui
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
  mensagem: string | null = null;

  constructor(private profissionalService: ProfissionalService) { }

  /**
   * Verifica se a senha é válida (mínimo de 8 caracteres, contendo letras e números).
   */
  senhaValida(): boolean {
    const senha = this.profissional.senha;
    return senha.length >= 8 && /\d/.test(senha) && /[A-Za-z]/.test(senha);
  }

  /**
   * Verifica se as senhas digitadas coincidem.
   */
  senhasIguais(): boolean {
    return this.profissional.senha === this.senhaRepetida;
  }

  /**
   * Envia o formulário, realiza validações e exibe mensagens de sucesso ou erro.
   */
  onSubmit() {
    if (!this.senhaValida()) {
      alert('A senha deve ter no mínimo 8 caracteres, incluindo letras e números.');
      return;
    }

    if (!this.senhasIguais()) {
      alert('As senhas não coincidem. Verifique os campos de senha.');
      return;
    }

    this.profissionalService.registerProfissional(this.profissional).subscribe({
      next: (response) => {
        console.log('Profissional cadastrado:', response);
        this.mensagem = 'Cadastro realizado com sucesso!';
        this.resetForm();
        this.exibirMensagemTemporaria();
      },
      error: (error) => {
        console.error('Erro ao cadastrar profissional:', error);
        this.mensagem = 'Erro ao cadastrar profissional.';
        this.exibirMensagemTemporaria();
      }
    });
  }

  /**
   * Reseta os campos do formulário.
   */
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

  /**
   * Exibe a mensagem de sucesso ou erro por um tempo limitado.
   */
  exibirMensagemTemporaria() {
    setTimeout(() => this.mensagem = null, 5000);
  }
}
