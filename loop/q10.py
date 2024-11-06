#10. Use a loop to count the number of digits in an integer.

num = int(input('Enter a digit: '))

count = 0

if num == 0:
    count = 1
else:
    while num != 0:
        num //= 10
        count += 1
print(f'The number of digits is: {count} ')
