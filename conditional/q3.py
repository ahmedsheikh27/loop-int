
# 3. Write a program that checks if a given year is a leap year.

year = int(input('Enter a year:'))

if year % 400 == 0:
    print(f'{year} is a leap year')
elif year % 100 == 0:
    print(f'{year} is not a leap year')
elif year % 4 == 0:
    print(f'{year} is a leap year')
else:
    print(year,' is not a leap year')