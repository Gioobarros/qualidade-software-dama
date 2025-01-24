import { Component, Injectable } from "@angular/core"
import { CadastroService, type Profissional, type Ong, User } from "../services/cadastro.service"
import { ValidadorCnpjService } from "../services/validador-cnpj.service"
import { CommonModule } from "@angular/common"
import { FormsModule } from "@angular/forms"
import { HeaderComponent } from "../components/header/header.component"

@Injectable({
  providedIn: "root",
})
@Component({
  selector: "app-cadastro",
  standalone: true,
  imports: [FormsModule, HeaderComponent, CommonModule],
  templateUrl: "./cadastro.component.html",
  styleUrls: ["./cadastro.component.css"],
})
export class CadastroComponent {
  tipoCadastro: "profissional" | "ong" = "profissional"

  profissional: Profissional = {
    nome_completo: "",
    cpf: "",
    conselho: "",
    contato: "",
    user: {
      password: "",
      username: "",
      email: "",
      perfil: "pro",
    },
    bio: "",
  }

  ong: Ong = {
    razao_social: "",
    cnpj: "",
    contato: "",
    user: {
      password: "",
      username: "",
      email: "",
      perfil: "ong",
    },
    bio: "",
  }

  senhaRepetida = ""
  mensagem: string | null = null

  constructor(
    private cadastroService: CadastroService,
    private validadorCnpjService: ValidadorCnpjService,
  ) {}

  updateLogin(value: string) {
    if (this.tipoCadastro === "profissional") {
      this.profissional.user.username = value
    } else {
      this.ong.user.username = value
    }
  }

  updateSenha(value: string) {
    if (this.tipoCadastro === "profissional") {
      this.profissional.user.password = value
    } else {
      this.ong.user.password = value
    }
  }

  updateContato(value: string) {
    if (this.tipoCadastro === "profissional") {
      this.profissional.contato = value
    } else {
      this.ong.contato = value
    }
  }

  updateEmail(value: string) {
    if (this.tipoCadastro === "profissional") {
      this.profissional.user.email = value
    } else {
      this.ong.user.email = value
    }
  }

  updateBio(value: string) {
    if (this.tipoCadastro === "profissional") {
      this.profissional.bio = value
    } else {
      this.ong.bio = value
    }
  }

  senhaValida(): boolean {
    const senha = this.tipoCadastro === "profissional" ? this.profissional.user.password : this.ong.user.password
    return senha.length >= 8 && /\d/.test(senha) && /[A-Za-z]/.test(senha)
  }

  senhasIguais(): boolean {
    const senha = this.tipoCadastro === "profissional" ? this.profissional.user.password : this.ong.user.password
    return senha === this.senhaRepetida
  }

  onSubmit() {
    if (!this.senhaValida()) {
      alert("A senha deve ter no mínimo 8 caracteres, incluindo letras e números.")
      return
    }

    if (!this.senhasIguais()) {
      alert("As senhas não coincidem. Verifique os campos de senha.")
      return
    }

    if (this.tipoCadastro === "profissional") {
      this.cadastrarProfissional()
    } else {
      this.validarECadastrarOng()
    }
  }

  cadastrarProfissional() {
    this.cadastroService.registerProfissional(this.profissional).subscribe({
      next: (response) => {
        console.log("Profissional cadastrado:", response)
        this.mensagem = "Cadastro de profissional realizado com sucesso!"
        this.voltarParaIndex()
        this.exibirMensagemTemporaria()
      },
      error: (error) => {
        this.mensagem = "Erro ao cadastrar profissional."
        this.exibirMensagemTemporaria()
      },
    })
  }

  validarECadastrarOng() {
    this.validadorCnpjService.validarCnpj(this.ong.cnpj).subscribe({
      next: (cnpjValido) => {
        if (cnpjValido) {
          this.cadastrarOng()
        } else {
          this.mensagem = "CNPJ inválido. Por favor, verifique o número informado."
          this.exibirMensagemTemporaria()
        }
      },
      error: (error) => {
        this.mensagem = "Erro ao validar CNPJ. Por favor, tente novamente mais tarde."
        this.exibirMensagemTemporaria()
      },
    })
  }

  cadastrarOng() {
    this.cadastroService.registerOng(this.ong).subscribe({
      next: (response) => {
        console.log("ONG cadastrada:", response)
        this.mensagem = "Cadastro de ONG realizado com sucesso!"
        this.voltarParaIndex()
        this.exibirMensagemTemporaria()
      },
      error: (error) => {
        this.mensagem = "Erro ao cadastrar ONG."
        this.exibirMensagemTemporaria()
      },
    })
  }

  exibirMensagemTemporaria() {
    setTimeout(() => (this.mensagem = null), 5000)
  }

  voltarParaIndex() {
    window.location.href = "/index"
  }
}

