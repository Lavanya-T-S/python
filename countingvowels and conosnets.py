def count(lst):
    count_vowels=0
    count_consonent=0
    vowels='aeiouAEIOU'


    for i in lst:

        if i in vowels:
            count_vowels+=1
        else :
            count_consonent+=1
    return count_vowels,count_consonent


lst=str(input("enter a word"))
count_vowels,count_consonent=count(lst)
print(count_vowels)
print(count_consonent)



