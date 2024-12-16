import uuid
from des import DesKey

id = str(uuid.uuid4())

id_8 = id[:8]

chave = DesKey(id_8.encode('utf-8'))

texto = 'texto'

texto = chave.encrypt('texto'.encode('utf-8'), padding=True)

print(texto)

outra_chave = DesKey(id_8.encode('utf-8'))

outro_texto = outra_chave.decrypt(texto, padding=True)

print(outro_texto.decode('utf-8'))
