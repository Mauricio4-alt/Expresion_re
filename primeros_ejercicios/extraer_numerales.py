import re

e = "#\w+"
text = "Hoy es un día soleado #Feliz #Verano2024"

match = re.findall(e,text)


print("felicidades",match)
