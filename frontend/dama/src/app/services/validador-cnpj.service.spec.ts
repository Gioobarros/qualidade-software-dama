import { TestBed } from '@angular/core/testing';

import { ValidadorCnpjService } from './validador-cnpj.service';

describe('ValidadorCnpjService', () => {
  let service: ValidadorCnpjService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ValidadorCnpjService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
