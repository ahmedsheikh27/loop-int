#7. Find the factorial of a number using a while loop.

num = int(input('Enter a digit: '))

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"The factorial of {num} is: {factorial}")
