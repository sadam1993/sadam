from itertools import count


a=5.22
quarter_value =.25
dime_value=.10
nickle_value=.05
penny_value=.01
dollar_amount= a
count_of_quarter =  dollar_amount//quarter_value
print("we need to give back",count_of_quarter,"quarters")
remaining_exchange_after_q=dollar_amount%quarter_value
count_of_dime=remaining_exchange_after_q//dime_value
print(count_of_dime,"dimes")
remaining_exchange_after_d=dollar_amount%dime_value
count_of_nickle=remaining_exchange_after_d//nickle_value
print(count_of_nickle,"nickle")
remaining_exchange_after_nickle=dollar_amount%nickle_value
count_of_pennies=remaining_exchange_after_nickle//penny_value

print(count_of_pennies,"pennies")





