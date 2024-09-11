monthlyIncome = int(input("What is your monthly income?"))

rent = int(input("How much does your rent cost per month?"))

utilities = int(input("How much do your bills cost per month?"))

groceries = int(input("How much do you spend on groceries per month?"))

transportation = int(input("How much does your transportation cost per month?"))

rentPercent = (rent/monthlyIncome)

utilPercent = (utilities/monthlyIncome)

grocPercent = (groceries/monthlyIncome)

commutePercent = (transportation/monthlyIncome)

savings = (monthlyIncome*0.20)

print("You should put " + str(savings) + " dollars into your savings account. This is 20 percent of your monthly income.")

print("Rent is " + str(rentPercent) + " percent of your monthly income.")

print("Utilities are " + str(utilPercent) + " percent of your monthly income.")

print("Groceries are " + str(grocPercent) + " percent of your monthly income.")

print("Commute is " + str(commutePercent) + " percent of your monthly income.")

accountAfter = int((monthlyIncome-(rent+utilities+groceries+transportation+savings)))

print("You have " + str(accountAfter) + " dollars left from your monthly income. Have fun!")

