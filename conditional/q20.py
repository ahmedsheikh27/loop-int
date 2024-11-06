
#20. Create a program that evaluates if an inputted number is prime.

prime = int(input('Enter a number: '))

if prime > 1:
    is_prime = True
    for i in range(2, int(prime**0.5) + 1):
        if prime % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f'The number {prime} is a prime number.')
    else:
        print(f'The number {prime} is not a prime number.')
else:
    print(f'The number {prime} is not a prime number.') 
