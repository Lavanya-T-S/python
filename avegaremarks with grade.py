def average(marks):
    total_marks=sum(marks)
    total_subjects=len(marks)
    average=total_marks/total_subjects
    return average

#calculate the grade and return it
def grade(average):
    if average>=80:
        grade="A"
    elif average>=60:
        grade="B"
    elif  average>=50:
        grade="C"
    else:
        grade="F"
    return grade


marks=[55,64,75,80,65]
average=average(marks)
print('Your average marks is: ', average)

grade=grade(average)
print("your grade is ",grade)
