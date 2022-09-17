print("please enter three ingredients")
s= input()
s=s.split()
print(s)
s1=s[0]
s2=s[1]
s3=s[2]
print("please enter a number:")
n=int(input())
print(s1,s2,s3)

f1=s1[0]
f2=s2[0]
f3=s3[0]
s1=str(n)+s1.removeprefix(f1)
n=n+1
s2=str(n)+s2.removeprefix(f2)
n=n+1
s3=str(n)+s3.removeprefix(f3)
print(s1,s2,s3)

