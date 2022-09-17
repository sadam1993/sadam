from cgi import print_arguments
from multiprocessing.sharedctypes import Value


a= 2.36

quarter_Value = .25
dime_value = .10
nickle_value = .05
penny_value = .01
count_of_quarters=(a//.25)
print("we need to give custamer",count_of_quarters,'quarters')
count_of_remaining_after_quarter=a%.25
count_of_dimes= count_of_remaining_after_quarter // dime_value
print(count_of_dimes,'dime')
count_of_remaining_after_dimes=a%.05
count_of_nickles=count_of_remaining_after_dimes //nickle_value
print(count_of_nickles,'nickles')
count_of_remaining_after_nickles=1
count_of_pennies=count_of_remaining_after_nickles
print(count_of_pennies,'pennies')
