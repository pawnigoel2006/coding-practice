def calculate_total(marks):
    return sum(marks)
def calculate_average(marks):
    return sum(marks)/len(marks)
def calculate_highest(marks):
    return max(marks)
def calculate_lowest(marks):
    return min(marks)
def check_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
def check_result(marks):
    if any(mark < 33 for mark in marks):
        return 'Fail'
    else:
        return 'Pass'
name=input("Enter the student's name: ")
marks=list(map(int,input("Enter the student's marks of 5 subjects separated by space: ").split()))
if len(marks) != 5:
    print("Please enter marks for exactly 5 subjects.")
elif any(mark < 0 or mark > 100 for mark in marks):
    print("Please enter valid marks between 0 and 100.")
else:
    total=calculate_total(marks)
    average=calculate_average(marks)
    highest=calculate_highest(marks)
    lowest=calculate_lowest(marks)
    grade=check_grade(average)
    result=check_result(marks)
    print(f"Student Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Percentage: {average:.2f}%")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print(f"Grade: {grade}")
    print(f"Result: {result}")