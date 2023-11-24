
def mergeAlternatively(word1: str,word2: str)->str:
    i,j=0,0
    res=[]
    while i<len(word1) and j<len(word2):
        res.append(word1[i])
        res.append(word2[j])
        i+=1
        j+=1
    res.append(word1[i:])
    res.append(word2[j:])
    return "".join(res)
lav = mergeAlternatively("abc", "pqr")
print(mergeAlternatively("abc","pqr"))

output:

C:\Users\ADMIN\.virtualenvs\sample\Scripts\python.exe "C:\Users\ADMIN\PycharmProjects\pythonProject1\sample\merge string alternately.py" 
apbqcr

Process finished with exit code 0