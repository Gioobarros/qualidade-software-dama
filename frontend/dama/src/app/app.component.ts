import { Component } from '@angular/core';
import { CadastroComponent } from './cadastro/cadastro.component'; 

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ CadastroComponent], 
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'dama';
}