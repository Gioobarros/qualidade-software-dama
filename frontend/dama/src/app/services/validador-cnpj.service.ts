import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

// token 1fdd39bda08c898cb238fbadd31d65a3f5447ee6619369b9aab1bb1cc4f27b34

@Injectable({
  providedIn: 'root'
})
export class ValidadorCnpjService {
  private apiUrl = 'https://publica.cnpj.ws/cnpj/';

  constructor(private http: HttpClient) { }

  validarCnpj(cnpj: string): Observable<boolean> {
    return this.http.get(`${this.apiUrl}${cnpj}`, {headers: {Accept: 'application/json', contentType: 'application/json'}}).pipe(
      map((resposta: any) => {
        // Se a API retornar um campo "status", significa que o CNPJ é válido
        return resposta?.estabelecimento?.situacao_cadastral == 'Ativa';
      })
    );
  }
}