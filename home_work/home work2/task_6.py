
print("enter a text")
text=input()
print("the text will start from the number you entered")
start=int(input())
print("the text will end at the number you entered")
end=int(input())

cut=text[(start-1):end]
print(cut)



