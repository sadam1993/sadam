a = 123
# find the mutliplication of digits of the number a
# number a will always have three digit number. 
# 2 * 3 * 4 = 24
# When we find remainder with 10, it will give us 
# the last digit of the number
# When I divide the number by 10 , it will remove the last digit
last_digit = a %10 # 3
print(last_digit)
# Following line will remove the last digit of variable a
a = a // 10 
middle_digit = a %10
a = a // 10 
first_digit = a % 10
multiplication = last_digit * middle_digit * first_digit
print("Multiplication result of all digit is",multiplication )



# Integer division will give us only the integer part of the division
# For example 
# 21 / 5 is 4.20 but if I use integer division operator 
# 21// 5 is 4


# b = 34
# print(b//10)  # 3

# c = 67
# print(c // 10) # 6

# d = 105 
# print(d//10) #10

# e = 1273
# print(e//10) # 127





