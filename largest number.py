def maximum(a,b):
    if a>b:
        return a
    else:
        return b


def funcInt(a,b,c,d,e,f):
    temp1=maximum(a,b)
    temp2=maximum(temp1,c)
    temp3=maximum(temp2,d)
    temp4 = maximum(temp3, e)
    largest=maximum(temp4,f)
    print(largest)
funcInt(11,1,8,14,16,20)


