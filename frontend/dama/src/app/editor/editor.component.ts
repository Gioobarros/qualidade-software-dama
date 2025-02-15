import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { EditorModule } from 'primeng/editor';

@Component({
  selector: 'app-editor',
  templateUrl: './editor.component.html',
  styleUrls: ['./editor.component.css'],
  standalone: true,
  imports: [FormsModule, EditorModule],
})
export class EditorComponent implements OnInit {
  text: string = '';

  ngOnInit() {
    // Inicialização, se necessário
  }
}