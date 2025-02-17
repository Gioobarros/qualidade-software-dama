import { Injectable } from "@angular/core"
import { HttpClient } from "@angular/common/http"
import { Observable } from "rxjs"
import { tap } from "rxjs/operators"

@Injectable({
  providedIn: "root",
})
export class AuthService {
  private apiUrl = "http://127.0.0.1:8000/api/login/" // URL da API

  constructor(private http: HttpClient) {}

  login(username: string, password: string): Observable<any> {
    return this.http.post<any>(this.apiUrl, { username: username, password: password }).pipe(
      tap((response) => {
        if (response && response.token) {
          localStorage.setItem("token", response.token)
        }
      }),
    )
  }

  logout() {
    localStorage.removeItem("token")
    localStorage.removeItem("username")
    localStorage.removeItem("perfil")
  }

  getToken(): string | null {
    return localStorage.getItem("token")
  }

  isLoggedIn(): boolean {
    return !!this.getToken()
  }
}

