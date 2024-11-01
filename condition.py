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

num = int(input('Enter a number: '))

check_validation = (num%3 or num%5) 

if check_validation == 0:
    print(f'Number {num} is a multiple of both 3 and 5' )
else:
    print(f'Number {num} is not a multiple of both 3 and 5') 