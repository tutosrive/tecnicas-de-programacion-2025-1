data_path = './manipulacion_archivos/explicacion/data/'

# Copiar una imagen usando modos binarios
with open(f'{data_path}/ingesrm.png', 'rb') as source:
    content = source.read() # Esta variable está definida "globalmente" por ello sirve en "línea 8"

with open(f'{data_path}/ingesrm_copy.png', 'wb') as destination:
    destination.write(content) # Escribe una nueva imagen