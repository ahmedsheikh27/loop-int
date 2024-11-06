
#4. Print the multiplication table of a given number.

table = int(input('Enter a digit: '))

for i in range(1, 11):
    print(f'The multiplication of ({table} x {i}) =  {table * i}')
