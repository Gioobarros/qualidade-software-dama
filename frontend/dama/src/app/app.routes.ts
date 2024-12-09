import { Routes } from '@angular/router';

export const routes: Routes = [
    {
      path: '', pathMatch: 'full', redirectTo: 'index'
    },
    {
      path: 'index',
      loadComponent: () => import('./index/index.component').then(i => i.IndexComponent)
    },
    {
      path: 'list',
      loadComponent: () => import('./list/list.component').then(l => l.ListComponent)
    },
    {
      path: 'login',
      loadComponent: () => import('./login/login.component').then(c => c.LoginComponent)
    },
    {
      path: 'cadastro',
      loadComponent: () => import('./cadastro/cadastro.component').then(c => c.CadastroComponent)
    },
    {
      path: 'relato',
      loadComponent: () => import('./relato/relato.component').then(r => r.RelatoComponent)
    },
    {
      path: 'relatos',
      loadComponent: () => import('./relatos/relatos.component').then(s => s.RelatosComponent)
    }

  ];
  