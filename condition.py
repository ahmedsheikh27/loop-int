# #1. Write a program that checks if a given number is positive, negative, or zero.
# num = int(input('Enter a number '))
# if num > 0:
#     print('Number is positive')
# elif num < 0:
#     print('Number is negative')
# else:
#     print("Number is zero")
# #2. Take a user’s age as input and display whether they are a minor, adult, or senior citizen.

# age = int(input('Please enter your age '))
# if age < 0:
#     print('Enter a invalid age')
# elif age  < 18:
#     print('Citizen is Minored age')
# elif age == 18:
#     print('Citizen is Adult')
# else:
#     print('Citizen is Senior')

# # 3. Write a program that checks if a given year is a leap year.

# year = int(input('Enter a year:'))

# if year % 400 == 0:
#     print(f'{year} is a leap year')
# elif year % 100 == 0:
#     print(f'{year} is not a leap year')
# elif year % 4 == 0:
#     print(f'{year} is a leap year')
# else:
#     print(year,' is not a leap year')

# # 4. Take an integer and check if it’s even or odd.

# num = int(input('Enter a number: '))

# if num % 2 == 0:
#     print(num,' is a even number')
# else:
#     print(num,' is a odd number')

# 5.Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).


# your_marks = float(input('Please enter the gained marks: '))
# total_marks = float(input('Please enter total marks: '))

# percentage = (your_marks / total_marks) * 100

# if percentage >= 90:
#     grade = 'A+'
# elif percentage >= 80:
#     grade = 'A'
# elif percentage >= 70:
#     grade = 'B'
# elif percentage >= 60:
#     grade = 'C'
# elif percentage >= 50:
#     grade = 'D'
# elif percentage >= 40:
#     grade = 'E'
# else:
#     grade = 'Fail'

# print(f'Percentage: {percentage:.2f}%')
# print(f'Grade: {grade}')

# 6. Write a program to find the largest of two numbers.
num_one = float(input('Enter the first number '))
num_two = float(input('Enter the second number '))

total = num_one + num_two
difference = num_two - num_one
middle_num = (total - difference) /2

if middle_num >= num_two:
    print(middle_num, 'is a largest number')
elif middle_num <= num_two:
    print(middle_num,' is a Lesser number' )
