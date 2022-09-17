
nums=[1,2,3,1,2,3,4,2,2,2,]
#remove all number 2's from the list

count=0
for number in nums:
    if number==2:
        count+=1
        print(count)

for i in range(count):
    nums.remove(2)
print(nums)
