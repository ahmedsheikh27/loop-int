
#14. Check if a year input by the user is a century year.

cen = int(input('Enter a year: '))

if cen % 100 == 0:
  print(f'The year {cen} is a century')
else:
  print(f'The year {cen} is not a century')