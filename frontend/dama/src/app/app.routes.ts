import { Routes } from '@angular/router';
import { RelatoComponent } from './relato/relato.component';
import { AuthGuard } from './auth.guard';

export const routes: Routes = [
    {
      path: '', pathMatch: 'full', redirectTo: 'index'
    },
    { path: 'relato', component: RelatoComponent, canActivate: [AuthGuard] },   // Tela protegida
    {
      path: 'redeapoio',
      loadComponent: () => import('./redeapoio/redeapoio.component').then(m => m.RedeapoioComponent)
    },
    {
      path: 'index',
      loadComponent: () => import('./index/index.component').then(i => i.IndexComponent)
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
      path: 'muraldeforca',
      loadComponent: () => import('./relatos/relatos.component').then(s => s.RelatosComponent)
    },
    {
      path: 'material',
      loadComponent: () => import('./material/material.component').then(r => r.MaterialComponent)
    },
    {
      path: 'relato/:id',
      loadComponent: () => import('./relato-detalhe/relato-detalhe.component').then(i => i.RelatoDetalheComponent)
    },
    { 
      path: 'relato', component: RelatoComponent, canActivate: [AuthGuard] 
    },
  ];
  