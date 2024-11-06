
#9. Take three sides of a triangle as input and check if they form a valid triangle.
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

is_valid_triangle = a + b > c and a + c > b and b + c > a

if is_valid_triangle:
 print(f"The sides form a valid triangle: ")
else:
    print("The sides do not form a valid triangle.")
