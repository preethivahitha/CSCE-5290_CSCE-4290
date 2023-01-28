import re

def date_valid(strings):
    date_regex1 = re.compile(r'^(Jan(?:uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2},\s+(19|20)\d{2}|^\d{1,2}-(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)[,]\s+(19|20)\d{2}|^(0[1-9]|1[0-2])[/](0[1-9]|[12][0-9]|3[01])[/](\d{2})$')
    date_regex2 = re.compile(r'([0-9]?[0-9])?[/]([0-9]?[0-9])?[/](\d{2,4})')
    match1 = date_regex1.findall(strings)
    match2 = date_regex2.findall(strings)
    if match1 :
        print('Date :', match1)
    if match2 :
        print('Date :', match2)