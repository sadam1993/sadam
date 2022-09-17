nums=[1,2,10,11,13,17,21,26]
sum=0
sum_odd=0
#from the given list find sum of all the even numbers
for number in nums:
    if number%2==0:
        sum+=number
    else:
        sum_odd+=number
print("sum of all even  number is",sum)        
print("sum of all odd number is",sum_odd)

