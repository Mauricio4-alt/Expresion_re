import re


p_nombre= re.compile(r'[sS]oy ([a-zA-z]+)')
P_cedula = re.compile(r' identificado con numero (\d+)')
p_edad = re.compile(r'tengo (\d{1,2}) años |edad (\d{1,2})')

texto = "Soy mauricio identificado con numero 123456, tengo 22 años "
nombre= ""
cedula = 0
edad = 0
if p_nombre.search(texto):
    nombre = p_nombre.search(texto).group(1)

if P_cedula.search(texto):
    cedula = P_cedula.search(texto).group(1)
if p_nombre.search(texto):
    edad = p_edad.search(texto).group(1)
print(nombre,edad,cedula,sep="\n")