import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private apiUrl = 'http://localhost:3000/signupUsersList'; // URL da sua API

  constructor(private http: HttpClient) {}

  // Método para fazer login
  login(email: string, password: string): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }
}