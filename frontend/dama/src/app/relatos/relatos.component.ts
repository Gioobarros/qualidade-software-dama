import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Component} from '@angular/core';
import { RelatosService} from '../services/relatos.service';
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
  styleUrls: ['./relatos.component.css']
})


export class RelatosComponent {

  listarRelatos(){
    
  }
}
