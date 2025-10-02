// auth.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, of } from 'rxjs';
import { tap, catchError, map } from 'rxjs/operators';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://127.0.0.1:8000/api/login/';
  private loggedIn = new BehaviorSubject<boolean>(this.isLoggedIn());

  constructor(
    private http: HttpClient,
    private router: Router
  ) {}

  // Observable para componentes se inscreverem
  isLoggedIn$ = this.loggedIn.asObservable();

  login(username: string, password: string): Observable<any> {
    return this.http.post<any>(this.apiUrl, { username, password }).pipe(
      tap(response => {
        this.handleLoginSuccess(response);
      }),
      catchError(error => {
        this.handleLoginError(error);
        return of(null);
      })
    );
  }

  private handleLoginSuccess(response: any): void {
    if (response?.token) {
      localStorage.setItem('token', response.token);
      localStorage.setItem('username', response.username);
      localStorage.setItem('perfil', response.perfil);
      this.loggedIn.next(true);
      this.router.navigate(['/']);
    }
  }

  private handleLoginError(error: any): void {
    console.error('Erro no login:', error);
    this.logout();
  }

  logout(): void {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    localStorage.removeItem('perfil');
    this.loggedIn.next(false);
    this.router.navigate(['/login']);
  }

  getToken(): string | null {
    return localStorage.getItem('token');
  }

  isLoggedIn(): boolean {
    return !!this.getToken();
  }

  // Validação opcional do token com o backend
  validateToken(): Observable<boolean> {
    const token = this.getToken();
    if (!token) return of(false);

    return this.http.get<{valid: boolean}>('http://127.0.0.1:8000/api/validate-token/', {
      headers: { Authorization: `Token ${token}` }
    }).pipe(
      map(response => response.valid),
      catchError(() => {
        this.logout();
        return of(false);
      })
    );
  }
}