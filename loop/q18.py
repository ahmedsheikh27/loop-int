#18. Use a loop to print numbers in reverse order within a given range.

num = int(input('Enter a number: '))

for i in range(num, 0 , -1):
    if num:
      print(f'The revese of the given number {num} {","} is {i} ')
    else:
      print('Please first enter a number')