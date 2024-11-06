
#11. Check if a given number is a multiple of both 3 and 5.

num = int(input('Enter a number: '))

check_validation = (num%3 or num%5) 

if check_validation == 0:
    print(f'Number {num} is a multiple of both 3 and 5' )
else:
    print(f'Number {num} is not a multiple of both 3 and 5') 
