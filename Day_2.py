#Tip Calculator
print("Welcome to the tip Calculator.\n")
total = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

new_total = total + total*tip/100
final_bill = round(new_total/5 , 2)
print(f"Each person should pay: {final_bill}")
