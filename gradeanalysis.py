marks=[55,64,75,80,65]
result=sum(marks)
average=result/len(marks)
if average>=80:
    print("A")
elif average>=60 and average<80:
    print("B")
elif average>=50 and average<60:
    print("C")
else:
    print("F")

