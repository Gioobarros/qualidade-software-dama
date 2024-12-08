import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; // Importando CommonModule

interface User {
  id: number;
  nome: string;
  tipoConta: string;
  contato: string;
  email: string;
}

@Component({
  selector: 'app-list',
  standalone: true,
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css'],
  imports: [CommonModule]
})
export class ListComponent {
  users: User[] = [
    { id: 1, nome: 'João Silva', tipoConta: 'Admin', contato: '(11) 98765-4321', email: 'joao@example.com' },
    { id: 2, nome: 'Maria Oliveira', tipoConta: 'Usuário', contato: '(11) 91234-5678', email: 'maria@example.com' },
    { id: 3, nome: 'Carlos Souza', tipoConta: 'Usuário', contato: '(11) 99876-5432', email: 'carlos@example.com' }
  ];

  deleteUser (userId: number): void {
    this.users = this.users.filter(user => user.id !== userId);
  }
}