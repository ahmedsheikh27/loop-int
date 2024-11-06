#14. Write a program that breaks the loop when a certain condition is met.

password = input('Enter your password: ')

symbols = '";:_./(@#)'
nums = '0123456789'
alphas = 'abcdefghijklmnopqrstuvwxyz'

has_symbols = False
has_nums = False
has_alphas = False

for requirments in password:
    if requirments in symbols:
        has_symbols = True
    elif requirments in nums:
        has_nums = True
    elif requirments in alphas:
        has_alphas = True
    if has_symbols and has_nums and has_alphas:
        break
if has_symbols and has_nums and has_alphas:
    print(f'The password "{password}" meets all condition')
else:
    print('The password does not meets the condition')       
