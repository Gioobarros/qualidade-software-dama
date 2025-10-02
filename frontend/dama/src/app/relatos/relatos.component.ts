import { FormsModule } from "@angular/forms"
import { CommonModule } from "@angular/common"
import { TruncatePipe } from "../truncate.pipe"
import { Component, type OnInit } from "@angular/core"
import { RelatosService, Relato } from "../services/relatos.service"
import { HeaderComponent } from "../components/header/header.component"
import { RouterLink, RouterModule } from "@angular/router"
import { DomSanitizer, SafeHtml } from "@angular/platform-browser"
import { CardModule } from "primeng/card"
import { ButtonModule } from "primeng/button"
import { DatePickerModule } from 'primeng/datepicker';
import { DatePicker } from 'primeng/datepicker';

@Component({
  selector: "app-relatos",
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    HeaderComponent,
    TruncatePipe,
    RouterModule,
    RouterLink,
    CardModule,
    ButtonModule,
    DatePickerModule,
    DatePicker,
  ],
  templateUrl: "./relatos.component.html",
  styleUrls: ["./relatos.component.css"],
})
export class RelatosComponent implements OnInit {
  mensagem = "";
  relatos: Relato[] = [];
  rangeDates: Date[] | undefined;  

  constructor(
    private relatosService: RelatosService,
    private sanitizer: DomSanitizer,
  ) {}

  ngOnInit(): void {
    this.relatosService.retrieveRelato().subscribe((response) => {
      if (response.status === 200) {
        this.relatos = response.body || []
        this.mensagem = "Os relatos foram carregados com sucesso!"
      } else {
        this.mensagem = "Não foi possível carregar os relatos."
      }
    })
  }

  sanitizeHTML(html: string): SafeHtml {
    return this.sanitizer.bypassSecurityTrustHtml(html)
  }

  
}

