import re

# vamos a validar que la dirección es un correo electrónico

correo ="Kjkirogap@compensar.com"


e = r"[\w.+_%-]+@\w+\.[\.\w]{2,}"

v_correo= re.search(e,correo)
if v_correo:
    r= v_correo.group()
    print(f"El correo electrónico {r} es correcto")
else:
    print('El correo electrónico no es correcto')