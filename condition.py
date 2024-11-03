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

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# if num1 > num2:
#     largest = num1
# else:
#     largest = num2

# print(f"The largest number is: {largest}")


#7
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# if num1 > num2 and num1 > num3:
#     largest = num1
# elif num2 > num1 and num2 > num3:
#     largest = num2
# else:
#     largest = num3

# print(f"The largest number is: {largest}")


#8. Create a program that checks if a given string is a palindrome.


#9. Take three sides of a triangle as input and check if they form a valid triangle.
# a = float(input("Enter the first side: "))
# b = float(input("Enter the second side: "))
# c = float(input("Enter the third side: "))

# is_valid_triangle = a + b > c and a + c > b and b + c > a

# if is_valid_triangle:
#  print(f"The sides form a valid triangle: ")
# else:
#     print("The sides do not form a valid triangle.")



#10. Write a program to determine if a given character is a vowel or consonant.

# word = input("Please enter a word: ")

# vowel = 'aeiou'
# find_vowel = []
# for vowels in word:
#  if vowels in vowel:
#   find_vowel.append(vowels)
# if find_vowel:
#     print(f'The word "{word}" has the following vowel(s): {", ".join(find_vowel)}.')
# else:
#     print(f'The word "{word}" has no vowels in it.')


#11. Check if a given number is a multiple of both 3 and 5.

# num = int(input('Enter a number: '))

# check_validation = (num%3 or num%5) 

# if check_validation == 0:
#     print(f'Number {num} is a multiple of both 3 and 5' )
# else:
#     print(f'Number {num} is not a multiple of both 3 and 5') 

# 12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.

# temp = float(input('Enter a temperature in Celcius: '))

# if temp <= 0:
#     print(f'The temperature is Freezing at {temp}C')
# elif  1 <= temp <= 25:
#     print(f'The temperature is Moderate at {temp}C')
# else:
#     print(f'The temperature is Hot at {temp}C')


#(

# 13. Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.

# num1 = float(input('Enter a number: '))

# operator = input('Enter an operator +,-,*,/: ')

# num2 = float(input('Enter a number: '))


# result = (num1 + num2 ) or (num1 - num2) or (num1 * num2) or (num1 / num2)

# if operator == '+':
#     result = num1 + num2
#     print(f'The result of {num1} + {num2} is {result}')
# elif operator == '-':
#     result = num1 - num2
#     print(f'The result of {num1} - {num2} is {result}')
# elif operator == '*':
#     result = num1 * num2
#     print(f'The result of {num1} * {num2} is {result}')
# elif operator == '/':
#     # Check if the second number is not zero to avoid division by zero
#     if num2 != 0:
#         result = num1 / num2
#         print(f'The result of {num1} / {num2} is {result}')
#     else:
#         print('Division by zero is not allowed.')
# else:
#     print('Please enter a valid operator (+, -, *, /)')
# adding new result logic

# new_num = float(input('Enter a new number: '))

# new_result = result + new_num or result - new_num or result / new_num or result * new_num 

# if result and operator == '+':
#     print(f'The result of {result} + {new_num} is {new_result}')
# elif result and operator == '-':
#     print(f'The result of {result} - {new_num} is {new_result}')
# elif result and operator == '*':
#     print(f'The result of {result} * {new_num} is {new_result}')
# elif result and operator == '/' :
#     if new_num == 0 :
#         print('The divion of a num with zero is not exist')
#     else:
#         print(f'The result of {result} / {new_num} is {new_result}') 
# else:
#     print('Please enter an valid operator like +, -, /, *')
# )

#14. Check if a year input by the user is a century year.

# cen = int(input('Enter a year: '))

# if cen % 100 == 0:
#   print(f'The year {cen} is a century')
# else:
#   print(f'The year {cen} is not a century')

#15. Write a program to check if a number is within a specified range.

# num_in_range = float(input('Enter a number to check its range: '))

# range_min = float(input('Enter min range: '))

# range_max = float(input('Enter max range: '))

# if range_min <= num_in_range <= range_max:
#     print(f'The number {num_in_range} is in the range of {range_min} to {range_max}')
# else:
#     print(f'The number {num_in_range} is not in the range of {range_min} to {range_max}')


#16. Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).
 
# a = float(input("Enter the first side: "))
# b = float(input("Enter the second side: "))
# c = float(input("Enter the third side: "))

# equilateral = a == b == c 

# scalene = b != c or a != b or c != a

# isosceles = a == b or a == c or b == c 

# if equilateral:
#     print("The three sides are equal, so the triangle is equilateral.")
# elif isosceles:
#     print("Two sides are equal, so the triangle is isosceles.")

# elif scalene:
#     print("All three sides are different, so the triangle is scalene.")

#17. Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.

# num = int(input('Enter a number: '))

# if num % 2 == 0 and num % 3 == 0:
#     print(f'The number {num} is the divisible of 2 and 3')
# elif num % 2 == 0:
#     print(f'The number {num} is the divisible of 2')
# elif num % 3 == 0:
#     print(f'The number {num} is the divisible of 3')
# else:
#     print(f'The number {num} is not a divisible of 2 and 3')

#18. Take a user’s score and determine if they pass or fail (pass if 50 or above).
 
# your_marks = float(input('Please enter the gained marks: '))
# total_marks = float(input('Please enter total marks: '))

# percentage = (your_marks / total_marks) * 100

# if 90 <= percentage <= 100:
#     grade = 'Pass'
# elif 50 <= percentage < 90:
#     grade = 'Pass'
# else:
#     grade = 'Fail'

# print(f'Percentage: {percentage:.2f}%')
# print(f'Grade: {grade}')

#19. Check if a string input is uppercase, lowercase, or a mix.

# user_input = input('Enter a string: ')

# if user_input.isupper():
#     print('Sting contain Upper Case')
# elif user_input.islower():
#     print('Sting contain Lower Case')
# elif any(x.isupper() for x in user_input) and any(x.islower() for x in user_input):
#     print('Sting contain both Upper and Lower keywords')
# else:
#     print('Input is Empty')

#20. Create a program that evaluates if an inputted number is prime.

# prime = int(input('Enter a number: '))

# if prime > 1:
#     is_prime = True
#     for i in range(2, int(prime**0.5) + 1):
#         if prime % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(f'The number {prime} is a prime number.')
#     else:
#         print(f'The number {prime} is not a prime number.')
# else:
#     print(f'The number {prime} is not a prime number.') 
