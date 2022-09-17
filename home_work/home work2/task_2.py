print("enter any text with spaces")
s3=input()
s3=s3.replace(" ","")
print(s3)

length=len(s3)
if length%2==0:
    print(False)
else:
    print(True)

