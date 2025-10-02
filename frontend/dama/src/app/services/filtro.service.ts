import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpResponse } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FiltroService {
  private apiUrl = 'http://127.0.0.1:8000/api/relato/';

  constructor(private http: HttpClient) {}

  // FiltroService
retrieveRelato(filters: any): Observable<any> {
  const params = new HttpParams({
    fromObject: {
      q: filters.searchTerm || '',
      startDate: filters.rangeDates?.[0]?.toISOString() || '',
      endDate: filters.rangeDates?.[1]?.toISOString() || ''
    }
  });
  
  return this.http.get('/api/relatos', { params });
}
}