
#17. Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

num = int(input('Enter a number: '))

if num % 2 == 0 and num % 3 == 0:
    print(f'The number {num} is the divisible of 2 and 3')
elif num % 2 == 0:
    print(f'The number {num} is the divisible of 2')
elif num % 3 == 0:
    print(f'The number {num} is the divisible of 3')
else:
    print(f'The number {num} is not a divisible of 2 and 3')
