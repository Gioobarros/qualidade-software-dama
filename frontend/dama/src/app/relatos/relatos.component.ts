import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Component, ViewChild, ElementRef} from '@angular/core';
import { RelatosService} from '../services/relatos.service';
import { Relato} from '../services/relato.service';
import { HeaderComponent } from '../components/header/header.component';

@Component({
  selector: 'app-relatos',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule, 
    HeaderComponent 
  ],
  templateUrl: './relatos.component.html',
  styleUrl: './relatos.component.css'
})


export class RelatosComponent {

}
