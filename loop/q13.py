#13. Use nested loops to print a pyramid pattern of *.

height = int(input("Enter the height of the pyramid: "))

for i in range(1, height + 1):
    print(" " * (height - i), end="")
    print("* " * i)
