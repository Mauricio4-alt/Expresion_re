import re

exp =r"[0-2][0-9][]\.\.\."
ip ="192.168.01"

result = re.findall(exp,ip)
if result:
    print(result)
else:
    print("esa no es una dirección ip")
