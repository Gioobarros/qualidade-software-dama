import { Component, type OnInit, Output, EventEmitter, Input } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { EditorModule } from "primeng/editor";

@Component({
  selector: "app-editor",
  templateUrl: "./editor.component.html",
  styleUrls: ["./editor.component.css"],
  standalone: true,
  imports: [FormsModule, EditorModule],
})
export class EditorComponent implements OnInit {
  @Input() text = "";
  @Output() textChange = new EventEmitter<string>();

  ngOnInit() {
    this.emitTextChange();
  }

  onTextChange() {
    // Pequeno delay para garantir que o conteúdo foi atualizado
    setTimeout(() => {
      this.emitTextChange();
    }, 0);
  }

  private emitTextChange() {
    if (!this.text) {
      this.textChange.emit("");
      return;
    }

    // Limpa o texto mantendo a formatação básica
    let cleanText = this.text
      .replace(/&nbsp;/g, " ")

    // Se o texto estiver vazio após a limpeza
    if (!cleanText || cleanText.trim() === "") {
      this.textChange.emit("");
      return;
    }

    // Verifica se há conteúdo real, não apenas tags HTML
    const tempDiv = document.createElement("div");
    tempDiv.innerHTML = cleanText;
    const textContent = tempDiv.textContent?.trim() || "";

    if (!textContent) {
      this.textChange.emit("");
      return;
    }

    this.textChange.emit(cleanText);
  }
}