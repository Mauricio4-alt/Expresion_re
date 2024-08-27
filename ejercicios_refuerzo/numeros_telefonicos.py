import re

exp =re.compile(r"\(?\d{3}\)?[. -]\d{3}[.-]\d{4}")
text = "Llámanos al (123) 456-7890 o al 123-456-7890 nuestra linea de bienestar es (444) 123-4596"

matches=exp.findall(text)
print(f'coincidencias {matches}')