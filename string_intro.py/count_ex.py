
#ask th user to give two different string values
#if the first string contains the second string
# return True,if not  return False

print("enter first string")
s1=input()

print("enter second string")
s2=input()

count_of_second=s1.count(s2)
is_contain=bool(count_of_second)
print(is_contain)

