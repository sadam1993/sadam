#exchange

from multiprocessing.sharedctypes import Value


quarter=.25
dime=.10
nickle=.05
penny=.01
count_of_quarters=5 
count_of_dimes=4
count_of_nickles=6
count_of_pennies=7
total_value=quarter*count_of_quarters+dime*count_of_dimes+nickle*count_of_nickles
+penny*count_of_pennies
print(quarter*count_of_quarters + dime*count_of_dimes + nickle*count_of_nickles + penny*count_of_pennies)







