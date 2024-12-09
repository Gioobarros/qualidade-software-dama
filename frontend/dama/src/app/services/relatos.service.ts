import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';


export interface Relato {
  id?: string;
  conteudo: string;
  // data_criacao: date
}

@Injectable({
  providedIn: 'root'
})


export class RelatosService {
  private apiUrl = 'http://127.0.0.1:8000/api/relato/'; 

  constructor(private http: HttpClient) { }

  // registerRelato(relato: Relato): Observable<HttpResponse<any>> {
  //   return this.http.get<any>(this.apiUrl, relato, {observe: 'response'});
  // }
}