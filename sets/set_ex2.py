
s={2,2,3,4,5,7}
s2={4,10,2,5,44}
print(min(s))
print(max(s2))
print(min(s))*(max(s2))
min=-200
count_of_iteration=0
for number in s:
    if count_of_iteration==0:
        min=number
    if number < min:
        min=number
    gcount_of_iteration+=1
print(min)
