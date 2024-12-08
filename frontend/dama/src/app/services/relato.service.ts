import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';


export interface Relato {
  id?: string;
  conteudo: string;
}

@Injectable({
  providedIn: 'root'
})


export class RelatoService {
  private apiUrl = 'http://127.0.0.1:8000/api/relato/'; 

  constructor(private http: HttpClient) { }

  registerRelato(relato: Relato): Observable<HttpResponse<any>> {
    return this.http.post<any>(this.apiUrl, relato, {observe: 'response'});
  }
}