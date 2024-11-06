    
#12. Print all prime numbers between 1 and 50.


for num in range(2, 50):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"The number {num} is a prime number.")