 #Q..Assignment: Personal Expense Calculator Build a Python program that asks the user 
#for: Name
#Monthly income Rent Food expenses Travel expenses Entertainment expenses Other expenses The program should calculate: 
#Total expenses Remaining money Savings percentage

a=str(input("enter your name: "))
b=float(input("monthly income: "))
c=float(input("rent: "))
d=float(input("food expenses: "))
e=float(input("transportation expenses: "))
f=float(input("entertainment expenses: "))
g=float(input("other expenses: "))
total_expenses = c + d + e + f + g 
print("Total expenses: ", total_expenses)
remaining_income = b - total_expenses
savings_percentage = (remaining_income / b) * 100
print("Remaining income: ", remaining_income)
print("Savings percentage: ", savings_percentage)

