import re
e = r"(https?)://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
text="Visita mi blog en https://www.miblog.com o sigue mi perfil en http://twitter.com/usuario y https://Telegram.com.co"

match = re.findall(e,text)


print(match)
