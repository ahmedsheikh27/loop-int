#16. Create a program to calculate the sum of the digits of an inputted integer.

num = int(input('Enter a number: '))

num_sum = 0

numbers = []
for i in range(1, num + 1):
        num_sum += i 

print(f"The sum of numbers {num} is = {num_sum}")
