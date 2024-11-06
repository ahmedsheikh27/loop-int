
# 13. Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.

num1 = float(input('Enter a number: '))

operator = input('Enter an operator +,-,*,/: ')

num2 = float(input('Enter a number: '))


result = (num1 + num2 ) or (num1 - num2) or (num1 * num2) or (num1 / num2)

if operator == '+':
    result = num1 + num2
    print(f'The result of {num1} + {num2} is {result}')
elif operator == '-':
    result = num1 - num2
    print(f'The result of {num1} - {num2} is {result}')
elif operator == '*':
    result = num1 * num2
    print(f'The result of {num1} * {num2} is {result}')
elif operator == '/':
    # Check if the second number is not zero to avoid division by zero
    if num2 != 0:
        result = num1 / num2
        print(f'The result of {num1} / {num2} is {result}')
    else:
        print('Division by zero is not allowed.')
else:
    print('Please enter a valid operator (+, -, *, /)')


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