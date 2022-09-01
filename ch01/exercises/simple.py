print(10*5)
print(10**5)
print(15/10)
print(15//10)
print(-15//10)
print(15%10)
print(10%15)
print(10%10)
print(0%10)
print(10/15) #Doesn't show that the decimal never ends. 

rateFloat = input ('Current exchange rate for the Euro to Dollar: ')

rate = float(rateFloat)

amountFloat = input("Amount of currency to exchange: ")

amount = float(amountFloat)

total = amount * rate

result = total - 3

print(result)
