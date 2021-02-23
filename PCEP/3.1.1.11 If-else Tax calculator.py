income = float(input("Enter the annual income: "))
standard = 85528
high_income = 14839.2

if income < standard: 
    tax = income * 0.18 -556.2
elif income > standard: 
    tax = (income - standard) * 0.32 + high_income 

tax = float(round(max(tax, 0)))
print("The tax is:", tax, "thalers")
