import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CadastroComponent } from './cadastro/cadastro.component';
import { HeaderComponent } from "./components/header/header.component"; 
import { ListComponent } from './list/list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CadastroComponent, RouterOutlet, HeaderComponent, ListComponent],
  template: `
  <app-header></app-header>
  <app-list></app-list>
  <app-cadastro></app-cadastro>
  <router-outlet></router-outlet>
  
  `
})
export class AppComponent {
  title = 'dama';
}