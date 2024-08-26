import re

e = r'\d{2}[-/]\d{2}[-/]\d{4}'
f ='14-07-2021 año en que nació nuestro pequeño mathias '

match = re.search(e,f)

if match:
    print(match.group())
else:
    print("No se ha ingresado la fecha")