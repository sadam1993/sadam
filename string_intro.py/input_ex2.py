
# user want to deposithis money to his bank account
# he already has $200 in his account
# he has three different paychecks (400,600,and $350)
# he can only deposit one paycheck at a time
# after he deposit all the money in the account 
# he bought a phone  for $599,and headphone for $299


bank_acc=200
print("please enter the first paycheck amountyou want to deposit")
first_deposit=int(input())
bank_acc += first_deposit
print("please enter the second paycheck amount you want to deposit")
second_deposit=int(input())
bank_acc += second_deposit
print("please enter the third paycheck amount you want to deposit")
third_deposit=int(input())
bank_acc+= third_deposit

print("please enter dollar amount of phone you want")
phone = int(input())
bank_acc  -= phone
  
print("please enter the dollar amount headphone you want ")
head_phone=int(input())
bank_acc -= head_phone
print("his final money in the bnak account",bank_acc)




