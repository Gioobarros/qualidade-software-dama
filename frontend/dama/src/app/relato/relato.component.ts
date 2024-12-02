import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Component, ViewChild, ElementRef} from '@angular/core';
import { RelatoService, Relato } from '../services/relato.service';


@Component({
  selector: 'app-relato',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule 
  ],
  templateUrl: './relato.component.html',
  styleUrls: ['./relato.component.css']
  
})


export class RelatoComponent /*implements AfterViewInit*/ {
  relato: Relato = {
    conteudo: ''
  };

  mostraConfirmacao: boolean = false;

  mostraResposta: boolean = false;

  mensagem: string = 'As informações escritas são de sua inteira responsabilidade vindo a ser monitorada em eventuais denúncias feitas por usuários. Comprovada alguma irregularidade, seu relato será excluído.'; 

  textoBotao: string = 'Entendo e desejo e publicar';

  eventoBotao: () => void =  this.enviaRelato; 
  
  // pegar um elemento dentro de um DOM de um jeito mais "anguloso"
  @ViewChild('relatoText') relatoText!: ElementRef;
  
  // construo o serviço
  constructor(private relatoService: RelatoService){}
  
  relatoConfirmacao() : void {
    this.mostraConfirmacao = true;
  }

  enviaRelato() : void{
    this.relatoService.registerRelato(this.relato).subscribe(
      (response) => {

      this.mensagem = response.status === 200 || response.status === 201 ? 
        'O relato foi registrado com sucesso!' : 'O relato não foi registrado!';
      this.textoBotao = 'Publicar outro relato'
      this.eventoBotao = this.retornar

      },
    );  
  }

  retornar() : void {
    this.relatoText.nativeElement.value = ''
    this.mostraConfirmacao = !this.mostraConfirmacao
    this.mensagem = 'As informações escritas são de sua inteira responsabilidade vindo a ser monitorada em eventuais denúncias feitas por usuários. Comprovada alguma irregularidade, seu relato será excluído.'
    this.textoBotao = 'Entendo e desejo e publicar'
    this.eventoBotao = this.enviaRelato

  }
}
