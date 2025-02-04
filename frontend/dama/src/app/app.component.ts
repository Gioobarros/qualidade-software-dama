import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CadastroComponent } from './cadastro/cadastro.component';
import { HeaderComponent } from './components/header/header.component';
import { ListComponent } from './list/list.component';
import { FooterComponent } from './components/footer/footer.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CadastroComponent,
    RouterOutlet,
    HeaderComponent,
    ListComponent,
    FooterComponent,
  ],
  template: `
    <div class="app-container">

      <div class="main-content">
        <router-outlet></router-outlet>
      </div>

      <app-footer></app-footer>
    </div>
  `,
})
export class AppComponent {
  title = 'dama';
}
