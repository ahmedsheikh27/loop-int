
#18. Take a user’s score and determine if they pass or fail (pass if 50 or above).
 
your_marks = float(input('Please enter the gained marks: '))
total_marks = float(input('Please enter total marks: '))

percentage = (your_marks / total_marks) * 100

if 90 <= percentage <= 100:
    grade = 'Pass'
elif 50 <= percentage < 90:
    grade = 'Pass'
else:
    grade = 'Fail'

print(f'Percentage: {percentage:.2f}%')
print(f'Grade: {grade}')
