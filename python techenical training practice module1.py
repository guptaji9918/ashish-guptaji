
a=str(input("enter your name: "))
b=float(input("monthly income: "))
c=float(input("rent: "))
d=float(input("food expenses: "))
e=float(input("transportation expenses: "))
f=float(input("entertainment expenses: "))
g=float(input("other expenses: "))
total_expenses = c + d + e + f + g # print("Total expenses: ", total_expenses)
remaining_income = b - total_expenses
savings_percentage = (remaining_income / b) * 100
print("Remaining income: ", remaining_income)
print("Savings percentage: ", savings_percentage)
remove unnecessary 
#Q.1. Take two numbers and print sum, difference, product and division. 
a=8
b=4
c=a+b
print(c)
c=a*b
print(c)
c=a-b
print(c)
c=a/b
print(c)

#2. Take the radius of a circle and calculate its area
r=8
area=3.14*r**2
print(area)


#3. Take the length and width of a rectangle and calculate its area. 
l=4
w=6
area=l*w
print(area)

#4. Convert Celsius to Fahrenheit. 
temp=38
f=9 * temp/5+32
print(f)

#5. Take marks of 5 subjects and calculate total and percentage. 
sub1 = int(input("enter marks in Maths:"))
sub2 = int(input("enter marks in Physics:"))
sub3 = int(input("enter marks in Chemistry:"))
sub4 = int(input("enter marks in Hindi:"))
sub5 = int(input("enter marks in English:"))
total_marks = sub1+sub2+sub3+sub4+sub5
print("Total Marks:", total_marks)
percentage = (total_marks/5)
print("Overall percentage(%):",percentage)

#6. Take the bill amount and calculate 18% GST. 
initial_price = float(input("Enter the initial price:"))
gst = initial_price * 0.18
bill_amount = initial_price + gst
print("Total bill amount:",bill_amount)


#7. Take salary and calculate salary after a 10% bonus.
salary = float(input("enter the salary amount:"))
bonus= salary*0.10
new_salary = salary+bonus
print("Salary with 10% bonus:", new_salary)


#8. Convert total minutes into hours and remaining minutes.
total_minutes = int(input("enter total minutes:"))
hours = total_minutes//60
minutes = total_minutes%60
print(f"Time--{hours}hr:{minutes}minutes")

#9. Take a three-digit number and calculate the sum of its digits. 
num = int(input("enter a 3-digits number:"))
if len(str(num))!=3:
 print("Not valid number. Re-enter only 3- digit number")
else: 
 digits_sum = (num//100) + ((num//10)%10) + num%10
print("sum of digits:", digits_sum)


#10. Take a number and determine its remainder when divided by 5. 
num = float(input("enter a number:"))
num%=5
print("Remainder when divided by 5:",num)


#11. Calculate simple interest. 
principle = int(input("Enter the principle amount:"))
rate = int(input("input rate(%):"))
time = int(input("enter time period (in years):"))
simple_interest = (principle*rate*time)/100
print("simple interest is:", simple_interest)

#13. Create a BMI calculator. 
weight = float(input("Enter your body weight:"))
height = float(input("Enter your height in metres:"))
BMI = weight/height
print(f"Body Mass Index(BMI) is {BMI} ")

#14. Create a salary calculator.
basic = int(input("enter basic salary :"))
pf = int(input("enter PF amount:"))
hra = int(input("enter HRA amount:"))
medical = int(input("enter medical allowances:"))
ta = int(input("enter travel Allowances:"))
net_salary = basic+pf+hra+medical+ta
print(f"Net salary is {net_salary}")



