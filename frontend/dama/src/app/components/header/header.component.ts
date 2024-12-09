import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { IndexComponent } from "../../index/index.component";


@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterLink, RouterOutlet, IndexComponent],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {

}
