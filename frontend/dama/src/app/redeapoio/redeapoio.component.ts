import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { HeaderComponent } from '../components/header/header.component';
import { FooterComponent } from '../components/footer/footer.component';

@Component({
  selector: 'app-redeapoio',
  standalone: true,
  imports: [HeaderComponent, FooterComponent],
  templateUrl: './redeapoio.component.html',
  styleUrl: './redeapoio.component.css'
})
export class RedeapoioComponent {

}
