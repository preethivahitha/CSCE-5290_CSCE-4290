import currency
import date
import phone_numbers
import tags

f = open('input.txt','r')
for li in f:
    print(li)
    print(phone_numbers.validNumber(li))
    tags.findTags(li)
    print(currency.Currency_valid(li))
    date.date_valid(li)