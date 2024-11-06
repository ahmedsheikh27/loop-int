#15. Print the sum of even and odd numbers separately up to a given number.

num = int(input('Enter a number: '))

even_num = 0
odd_num = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        even_num += i
    else:
        odd_num += i
        
print(f"The sum of even numbers up to {num} is: {even_num}")
print(f"The sum of odd numbers up to {num} is: {odd_num}")

