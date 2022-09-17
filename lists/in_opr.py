#using in opera




list=[1,2,3,4,5,]

if 2 in list:
    print("2 is in the list")
if 11 in list:
    print(11,"is in list")
# not in operator will check if the specified value is not in the 
# iterable objects.
if 6 not in list:
    print( 6, "is not in the list")




print("enter  arandom digit")
digit =int(input())
if digit in list:
    print("you have won a prize")
elif digit not in list:
    print("may be next time")
 

