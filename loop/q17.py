#17. Write a program that continues to ask for a number until the correct number is guessed.

guess_num = 5

num = int(input('Guess the number from 1-10: '))

if num == guess_num:
    print(f'The number {num} is correct and equal to the guessed num: {guess_num}')
else:
    print(f'The correct number is {guess_num}')
