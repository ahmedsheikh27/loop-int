
#15. Write a program to check if a number is within a specified range.

num_in_range = float(input('Enter a number to check its range: '))

range_min = float(input('Enter min range: '))

range_max = float(input('Enter max range: '))

if range_min <= num_in_range <= range_max:
    print(f'The number {num_in_range} is in the range of {range_min} to {range_max}')
else:
    print(f'The number {num_in_range} is not in the range of {range_min} to {range_max}')
