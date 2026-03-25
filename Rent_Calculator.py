rent = int(input("Enter the rent of the flat : "))
maintenance = int(input("Enter the maintenance of the flat : "))
food = int(input("Enter the food expenses of the month : "))
groceries = int(input("Enter the groceries expenses of the month : "))
wifi = int(input("Enter the wifi expenses of the month : "))
electricity_bill = int(input("Enter the electricity bill of the month : "))
gas = int(input("Enter the gas bill of the month : "))
persons = int(input("Enter the number of persons in the flat : "))

# total expenses
total_expense = rent + maintenance + food + groceries + wifi + electricity_bill + gas
each_person = total_expense / persons

print("\nTotal flat expense =", total_expense)
print("Each person should pay =", each_person)