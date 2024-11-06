#20. Create a program that simulates a countdown timer starting from a given number down to zero.
import time

num = int(input('Enter the timer: '))

for i in range(num , -1, -1):
    print(i)
    time.sleep(1)

print('Countdown Complete!!')