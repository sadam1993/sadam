



from enum import unique


print("enter string")
str=input()

# we should check for each letter, if there is duplication
index=0
while index<len(str):
    if str.count(str[index])>1:
        #it means there is duplicated letter
        is_unique=False
        break
    index+=1
if is_unique==True:   
    print("string consists of unique letters")
else:
    print("string has duplicated letters")
