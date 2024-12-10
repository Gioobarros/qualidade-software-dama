import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { TruncatePipe } from '../truncate.pipe';
import { Component, OnInit} from '@angular/core';
import { RelatosService, Relato } from '../services/relatos.service';
import { HeaderComponent } from '../components/header/header.component';
import { Router, RouterLink, RouterModule } from '@angular/router';

@Component({
  selector: 'app-relatos',
  standalone: true,
  imports: [CommonModule, FormsModule, HeaderComponent, TruncatePipe, RouterModule, RouterLink ],
  templateUrl: './relatos.component.html',
  styleUrls: ['./relatos.component.css']
})


export class RelatosComponent implements OnInit{
  // crio a lista de relatos

  mensagem: string = ""

  relatos: Relato[] = []



  constructor(private relatosService: RelatosService) {} // construo o serviço

  // função que traz os relatos
  ngOnInit(): void{

    this.relatosService.retrieveRelato().subscribe((response) =>{

      if(response.status === 200){

        this.relatos = response.body || []

        this.mensagem = 'Os relatos foram carregados com sucesso!'

      }

      else
        this.mensagem = 'Não foi possível carregar os relatos.';
      
    })
  }

}
