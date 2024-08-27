import re


expression = re.compile(r"^[\w$%!_\.-]+@[A-Za-z]+(\.[a-z]{2,5}+)$")
correo ="correo@dominio.com"
match = expression.search(correo)
if match!=None:
    print("¡Felicidades!,es un correo valido ")
    print(match.group())
else: 
    print("Esa es una dirección de correo inválida")
    