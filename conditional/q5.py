#5.Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

your_marks = float(input('Please enter the gained marks: '))
total_marks = float(input('Please enter total marks: '))

percentage = (your_marks / total_marks) * 100

if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
elif percentage >= 40:
    grade = 'E'
else:
    grade = 'Fail'

print(f'Percentage: {percentage:.2f}%')
print(f'Grade: {grade}')

