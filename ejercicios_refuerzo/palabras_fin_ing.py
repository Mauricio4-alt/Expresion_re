import re

exp= r'[A-Za-z]*ing'

text = "\"I am running and jumping while singing.\" bingbingbing"


result = re.findall(exp,text)

print(result)