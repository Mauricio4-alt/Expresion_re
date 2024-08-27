import re


exp =r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[*#$%!|@])([\w*#$%!|@])+$'
text ="Contr4señ4123@!"
result= re.match(exp,text)

if result:
    print("Contraseña fuerte")
else:
    print("Contraseña débil")