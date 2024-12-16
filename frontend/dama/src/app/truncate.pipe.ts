import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'truncate',
  standalone: true
})

export class TruncatePipe implements PipeTransform {

  transform(texto: string, limite: number, fim: string = '...'): string {

    if(!texto)
      return ''
    
    return texto.length > limite ? texto.substring(0, limite)+ fim : texto;
    
  }

}
