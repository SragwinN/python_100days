print("Welcome to the tip calculator!")
Bill = float(input("What was the total bill?$"))
Tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
Tip_as_percentage = Tip/100
Bill_with_tip = Bill*Tip_as_percentage + Bill
people = int(input("How many people to split the bill?"))
Total_Bill = Bill_with_tip / people
bill_per_person = round(Total_Bill,2)
bill_per_person = "{:.2f}".format(Total_Bill)
print(f"Each person should pay: ${bill_per_person}")






