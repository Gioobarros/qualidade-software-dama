import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-cadastro',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './cadastro.component.html',
})
export class CadastroComponent {
  tipoCadastro: string = '';
  cadastro: any = {
    nome: '',
    email: '',
    senha: '',
    contato: '',
    cnpj: '',
    bio: '',
    cpf: '',
    conselho: '',
  };

  onSubmit(form: any): void {
    console.log('Formulário submetido:', form.value);
  }

  cancelar(): void {
    console.log('Operação cancelada');
  }
}
