import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Profissional {
  id?: string;
  nome_completo: string;
  cpf: string;
  login: string;
  senha: string;
  conselho: string;
  contato: string;
  email: string;
  bio: string;
}

@Injectable({
  providedIn: 'root'
})
export class ProfissionalService {
  private apiUrl = 'http://127.0.0.1:8000/api/profissional/'; 

  constructor(private http: HttpClient) { }

  registerProfissional(profissional: Profissional): Observable<Profissional> {
    return this.http.post<Profissional>(this.apiUrl, profissional);
  }
}