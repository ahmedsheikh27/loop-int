
#2. Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

age = int(input('Please enter your age '))
if age < 0:
    print('Enter a invalid age')
elif age  < 18:
    print('Citizen is Minored age')
elif age == 18:
    print('Citizen is Adult')
else:
    print('Citizen is Senior')