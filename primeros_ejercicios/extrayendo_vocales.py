import re

e = re.compile(r"\b[aeiouAEIOU]\w+\b")
text = "Hola, esta es una oración de ejemplo"
result = e.findall(text)


print(result)

