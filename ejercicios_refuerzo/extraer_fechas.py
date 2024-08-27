import re

ex = r'\d{1,3}[-/]\d{1,3}[-/]\d{4}'
text = "Hoy es 4-8-2024 y mañana será 5/8/2024"
matches =re.findall(ex,text)

print(f"coincidencias {matches}")