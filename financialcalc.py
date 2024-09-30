def question(type):
    return int(input(f"Monthly {type}"))

monthlyIncome = question("income")

rent = question("rent")

utilities = question("utilities")

groceries = question("groceries")

transportation = question("transportation")

rentPercent = (rent/monthlyIncome)

utilPercent = (utilities/monthlyIncome)

grocPercent = (groceries/monthlyIncome)

commutePercent = (transportation/monthlyIncome)

savings = (monthlyIncome*0.15)

accountAfter = int((monthlyIncome-(rent+utilities+groceries+transportation+savings)))

expenses = int(rent+utilities+transportation+groceries+savings)

def percent(type, amount):
    per = amount/monthlyIncome*100
    print(f"Your {type} is {per}% income.")

print(f"You should put " + str(savings) + " dollars into your savings account. This is 15 percent of your monthly income.")

print(f"You have " + str(accountAfter) + " dollars left from your monthly income. Have fun!")

print(f"Your monthly income is $" + str(monthlyIncome) + ".")

print(f"Your expenses are $" + str(expenses) + ".")

percent("rent", rent)

percent("groceries", groceries)

percent("utilities", utilities)

percent("commute", transportation)



