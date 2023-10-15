def log(number):
    large=number[0]
    for i in number:
        if (i>large):
            large=i
        return large

number=[9,7,4,6,0,1,3,5]
large=log(number)
print(large)
