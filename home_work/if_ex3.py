

print("emter a date in format of month/day/year")


print("date in format of month/day/year""mm/dd/yyyy")
date=input()
month=date[0:2]
day=date[3:5]
year=date[-4:]

if month == "01": 
    print(f"january{day},{year}")
elif month =="2":
    print(f"february{day},{year}")



