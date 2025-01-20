import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ValidadorCnpjService {
  private apiUrl = 'https://receitaws.com.br/v1/cnpj/';

  constructor(private http: HttpClient) { }

  validarCnpj(cnpj: string): Observable<boolean> {
    return this.http.get(`${this.apiUrl}${cnpj}`).pipe(
      map((resposta: any) => {
        // Se a API retornar um campo "status", significa que o CNPJ é válido
        return resposta.status !== 'ERROR';
      })
    );
  }
}

