import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';


export interface Relato {
  id?: string;
  conteudo: string;
  data_criacao: Date;
}

@Injectable({
  providedIn: 'root'
})


export class RelatosService {
  private apiUrl = 'http://127.0.0.1:8000/api/relato/'; 

  constructor(private http: HttpClient) { }

  retrieveRelato(): Observable<HttpResponse<Relato[]>> {
    return this.http.get<Relato[]>(this.apiUrl, {observe: 'response' });
  }

  // retrieveRelato(params?: any): Observable<Relato[]> {
  //   return this.http.get<Relato[]>(this.apiUrl, { params });
  // }
  
  // // Exemplo de uso
  // this.relatosService.retrieveRelato({ search: 'termo' }).subscribe(relatos => {
  //   console.log(relatos);
  // });
  
}