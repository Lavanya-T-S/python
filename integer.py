a=list((123,123.5,"123",12+4j,1-6.0j,178,"python"))
for i in a:
    if (type(i) == int):
        print(i)

        or

def listfunc(j):
    for i in j:
        if (type(i) ==int):
            print(i)
listfunc((123,123.5,"123",12+4j,1-6.0j,178,"python"))