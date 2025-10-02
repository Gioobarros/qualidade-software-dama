import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { IndexComponent } from "../../index/index.component";
import { AuthService } from '../../services/auth.service';
import { CommonModule } from '@angular/common';
import { ButtonModule } from 'primeng/button'; 


@Component({
  selector: 'app-header',
  standalone: true,
  imports: [RouterLink, RouterOutlet, IndexComponent, CommonModule, ButtonModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {
  constructor(public authService: AuthService) {} 
}
