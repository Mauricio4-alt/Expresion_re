import re

expression = re.compile("tonto|malo|feo|inutil")
text = "mi amigo el feo es demasiado tonto y malo en su trabajo"
def replace_with_asterisk(match):
    return "*"*len(match.group())
result =expression.sub(replace_with_asterisk,text)

print(result)
