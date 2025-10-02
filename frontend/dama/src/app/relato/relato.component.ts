import { FormsModule } from "@angular/forms"
import { CommonModule } from "@angular/common"
import { RouterLink, RouterOutlet } from "@angular/router"
import { Component, OnInit } from "@angular/core"
import { RelatoService, Relato } from "../services/relato.service"
import { HeaderComponent } from "../components/header/header.component"
import { Router } from "@angular/router"
import { EditorComponent } from "../editor/editor.component"

@Component({
  selector: "app-relato",
  standalone: true,
  imports: [CommonModule, FormsModule, HeaderComponent, RouterLink, RouterOutlet, EditorComponent],
  templateUrl: "./relato.component.html",
  styleUrls: ["./relato.component.css"],
})
export class RelatoComponent implements OnInit {
  relato: Relato = {
    conteudo: "",
    publicador: "",
  }

  mostraConfirmacao = false
  mostraResposta = false
  mensagem =
    "As informações escritas são de sua inteira responsabilidade vindo a ser monitorada em eventuais denúncias feitas por usuários. Comprovada alguma irregularidade, seu relato será excluído."
  textoBotao = "Entendo e desejo publicar"

  constructor(
    private relatoService: RelatoService,
    private router: Router,
  ) {}

  ngOnInit() {
    this.relato.publicador = localStorage.getItem("username") || ""
  }

  relatoConfirmacao(): void {
    // Verifica se há conteúdo real, não apenas espaços em branco ou tags HTML vazias
    const tempDiv = document.createElement("div");
    tempDiv.innerHTML = this.relato.conteudo;
    const textContent = tempDiv.textContent?.trim() || "";

    if (!textContent) {
      this.mensagem = "O conteúdo do relato não pode estar vazio."
      this.mostraConfirmacao = true
      this.textoBotao = "Voltar e editar"
      this.eventoBotao = () => (this.mostraConfirmacao = false)
    } else {
      this.mostraConfirmacao = true
      this.mensagem =
        "As informações escritas são de sua inteira responsabilidade vindo a ser monitorada em eventuais denúncias feitas por usuários. Comprovada alguma irregularidade, seu relato será excluído."
      this.textoBotao = "Entendo e desejo publicar"
      this.eventoBotao = () => this.enviaRelato()
    }
  }

  updateRelatoContent(content: string) {
    this.relato.conteudo = content;
    console.log("Conteúdo atualizado:", content); // Para debug
  }

  enviaRelato(): void {
    const tempDiv = document.createElement("div");
    tempDiv.innerHTML = this.relato.conteudo;
    const textContent = tempDiv.textContent?.trim() || "";

    if (!textContent) {
      this.mensagem = "O conteúdo do relato não pode estar vazio."
      return
    }

    this.relatoService.registerRelato(this.relato).subscribe({
      next: (response) => {
        if (response.status === 200 || response.status === 201) {
          this.mensagem = "O relato foi registrado com sucesso!"
          setTimeout(() => {
            this.router.navigate(["/muraldeforca"])
          }, 1500)
        } else {
          this.mensagem = "O relato não foi registrado!"
        }
      },
      error: (error) => {
        console.error("Erro ao enviar relato:", error)
        this.mensagem = "Ocorreu um erro ao enviar o relato."
      }
    })
  }

  eventoBotao: () => void = () => this.enviaRelato()
}