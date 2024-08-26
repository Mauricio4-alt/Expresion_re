import re 

e = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

text = "Mi@C4rbaj4l*"
res = re.compile(e)
match =res.search(text)

if match:
    
    print("contraseña fuerte")
else:
    print("Contraseña Débil")


