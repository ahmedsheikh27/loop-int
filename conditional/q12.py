
# 12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.

temp = float(input('Enter a temperature in Celcius: '))

if temp <= 0:
    print(f'The temperature is Freezing at {temp}C')
elif  1 <= temp <= 25:
    print(f'The temperature is Moderate at {temp}C')
else:
    print(f'The temperature is Hot at {temp}C')
