
#19. Check if a string input is uppercase, lowercase, or a mix.

user_input = input('Enter a string: ')

if user_input.isupper():
    print('Sting contain Upper Case')
elif user_input.islower():
    print('Sting contain Lower Case')
elif any(x.isupper() for x in user_input) and any(x.islower() for x in user_input):
    print('Sting contain both Upper and Lower keywords')
else:
    print('Input is Empty')
