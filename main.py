from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = int(input("Enter the amount: ")) 
from_currency = input ("From currency: ").upper()
to_currency = input ("To currency: ").upper()

print(from_currency, "To",to_currency, amount)
result = c.convert(from_currency, to_currency, amount)
print(result)
