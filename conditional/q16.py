
#16. Take the length of three sides and classify the triangle (equilateral, isosceles, or scalene).
 
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

equilateral = a == b == c 

scalene = b != c or a != b or c != a

isosceles = a == b or a == c or b == c 

if equilateral:
    print("The three sides are equal, so the triangle is equilateral.")
elif isosceles:
    print("Two sides are equal, so the triangle is isosceles.")

elif scalene:
    print("All three sides are different, so the triangle is scalene.")
