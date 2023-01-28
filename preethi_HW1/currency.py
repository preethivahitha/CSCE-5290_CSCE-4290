import re
currency_regex  = r'\$[0-9]+(?:,[0-9]{3})*(?:\.[0-9]{2})?(?:M|B|K)?|[-+]\$[0-9]+(?:,[0-9]{3})*(?:\.[0-9]{2})?|[USD]{2,3}[0-9]+(?:M|B|K)'
def Currency_valid(s):
    pattern = re.compile(currency_regex)
    currency_match = pattern.findall(s)
    if currency_match:
        print( currency_match)
    

# Currency_valid('$954.49 is valid $10,724.00 idjkd $1,000,000,023.45')