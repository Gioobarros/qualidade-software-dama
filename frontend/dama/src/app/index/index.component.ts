import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { HeaderComponent } from '../components/header/header.component';
import { MaterialComponent } from "../material/material.component";

@Component({
  selector: 'app-index',
  standalone: true,
  imports: [RouterLink, RouterOutlet, HeaderComponent, MaterialComponent],
  templateUrl: './index.component.html',
  styleUrl: './index.component.css'
})
export class IndexComponent {

}
