import { Injectable } from "@angular/core"
import { HttpClient } from "@angular/common/http"
import { Observable } from "rxjs"

export interface User {
  password: string
  username: string
  email: string
  perfil: string
}

export interface Profissional {
  id?: string
  nome_completo: string
  cpf: string
  conselho: string
  contato: string
  bio: string
  user: User
}

export interface Ong {
  id?: string
  razao_social: string
  cnpj: string
  contato: string
  bio: string
  user: User
}

@Injectable({
  providedIn: "root",
})
export class CadastroService {
  private apiUrlProfissional = "http://127.0.0.1:8000/api/profissional/"
  private apiUrlOng = "http://127.0.0.1:8000/api/ong/"

  constructor(private http: HttpClient) {}

  registerProfissional(profissional: Profissional): Observable<Profissional> {
    return this.http.post<Profissional>(this.apiUrlProfissional, profissional)
  }

  registerOng(ong: Ong): Observable<Ong> {
    return this.http.post<Ong>(this.apiUrlOng, ong)
  }
}

