import re

def validNumber(data):
    p = r'^(?:\+?1[\s.-]?)?(?:\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}$|\d{3}-\d{3}-\d{3}-\d{4}'
    pattern = re.compile(p)
    match = pattern.finditer(str(data))
    return match

# print(validNumber("this is 6012664949"))