student = input()
grades_counter = 0
years_counter = 0
failed_years_counter = 0

while True:
    annual_grade = float(input())
    if annual_grade < 4:
        failed_years_counter += 1
        if failed_years_counter > 1:
            print(f'{student} has been excluded at {years_counter + 1} grade')
            break
        continue

    years_counter += 1
    grades_counter += annual_grade

    if years_counter == 12:
        if years_counter != 0:
            average_grade = f'{grades_counter / years_counter:.2f}'
            print(f'{student} graduated. Average grade: {average_grade}')
        else:
            print(f'{student} has been excluded at 1 grade')
        break
