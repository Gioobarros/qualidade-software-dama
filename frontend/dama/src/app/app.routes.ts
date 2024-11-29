import { Routes } from '@angular/router';

export const routes: Routes = [
    {
      path: '', pathMatch: 'full', redirectTo: 'login'
    },
    {
      path: 'list',
      loadComponent: () => import('./list/list.component').then(r => r.ListComponent)
    },
    {
      path: 'login',
      loadComponent: () => import('./login/login.component').then(c => c.LoginComponent)
    }
  ];
  