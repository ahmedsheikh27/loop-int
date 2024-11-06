
# 5. Print all odd numbers between 1 and 100 using a loop.
num = 1  # First method
while num <= 100:
    if num % 2 != 0:
        print(f'The number {num} is a odd number.')
    num += 1 
num = 1
#with for loop
for i in range(num, 100): # Second method
    if i % 2 != 0:
      print(f'The number {i} is a odd number.')
