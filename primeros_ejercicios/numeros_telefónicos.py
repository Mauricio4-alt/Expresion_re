import re

r = re.compile(r'(\+?\d{1,3})?[-. ]?(\(?\d{3}\)?)[-. ]\d{3}[-. ]\d{4}$')
text ='414.159.9642'

res=r.search(text)

if res:
    print(res.group())