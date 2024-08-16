import re

# patron = re.compile('a[3-5]+') # coincide con una letra, seguida de al menos 1 dígito entre 3 y 5
#match devuelve None si no coincide al inicio de la cadena
# m= patron.match('abb345')
# print(m)
# busca por toda la cadena alguna coincidencia.
# s= patron.search('abba345')
# print(s)

# for m in patron.finditer("a455 a333b435"):
#     print(m)

# patron = re.compile('([ab])?')
# matcher = patron.search('ab455 a333b435')
# grupo_cero= matcher.group(0)
# print(grupo_cero)
# grupo_uno= matcher.group(1)
# print(grupo_uno)
# grupo_dos= matcher.group(2)
# print(grupo_dos)
# grupo_tres= matcher.groups()
# print(grupo_tres)


texto = "Antonio Lopez Identificado con cédula de ciudadanía No 1234 de Bogotá, Pedro Garcia con cédula No 5678."

# Patrón para nombre y cédula
patron = r"([A-Z][a-z]+ [A-Z][a-z]+).*?cédula de ciudadanía No (\d+)"

matches = re.findall(patron, texto)

for match in matches:
    nombre, cedula = match
    print(f"Nombre: {nombre}, Cédula: {cedula}")
