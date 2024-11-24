import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CadastroComponent } from './cadastro/cadastro.component'; 

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ CadastroComponent, RouterOutlet],
  template: `
  <app-cadastro></app-cadastro>
  <router-outlet></router-outlet>
  
  `
})
export class AppComponent {
  title = 'dama';
}