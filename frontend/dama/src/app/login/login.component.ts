import { Component } from "@angular/core"
import { HeaderComponent } from "../components/header/header.component"
import { FormsModule } from "@angular/forms"
import { CommonModule } from "@angular/common"
import { Router } from "@angular/router"
import { AuthService } from "../services/login.service"

@Component({
  selector: "app-login",
  standalone: true,
  imports: [HeaderComponent, FormsModule, CommonModule],
  templateUrl: "./login.component.html",
  styleUrl: "./login.component.css",
})
export class LoginComponent {
  username = ""
  password = ""

  constructor(
    private authService: AuthService,
    private router: Router,
  ) {}

  onSubmit() {
    if (this.username && this.password) {
      this.authService.login(this.username, this.password).subscribe(
        (response) => {
          console.log("Login bem-sucedido", response)
          localStorage.setItem("token", response.token)
          localStorage.setItem("username", response.username)
          localStorage.setItem("perfil", response.perfil)
          this.router.navigate(["/dashboard"])
        },
        (error) => {
          console.error("Erro no login:", error)
          // Adicione aqui a lógica para mostrar uma mensagem de erro ao usuário
        },
      )
    } else {
      console.error("Username ou password não preenchidos")
      // Adicione aqui a lógica para mostrar uma mensagem de erro ao usuário
    }
  }
}

