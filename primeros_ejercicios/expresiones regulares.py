import re

# Compilando las expresiones regulares
p_nombre = re.compile(r'([A-Za-z]+(?:\s[A-Za-z]+)?)(?=\s+identificado| con el numero)')

# Ejemplos de textos
texto1 = "Soy Mauricio identificado con numero 123456, tengo 22 años "
texto2 = "Mauricio Urdaneta identificado con cedula 123456 con 22 años de edad"

# Buscando en los textos
coincide_nombre1 = p_nombre.search(texto1)
coincide_nombre2 = p_nombre.search(texto2)

# Extrayendo y mostrando los nombres
if coincide_nombre1:
    nombre1 = coincide_nombre1.group(1).strip()
    print(f"Nombre en texto1: {nombre1}")

if coincide_nombre2:
    nombre2 = coincide_nombre2.group(1).strip()
    print(f"Nombre en texto2: {nombre2}")
