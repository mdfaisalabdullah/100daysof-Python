###############
## tip calculator

# bill distribution amongs friiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiends

print("Hello, Welcome to the Tip calculator.")
bill = float(input("What is your total bill? $"))
numof_friends = int(input("How many friends are there?"))
tip = int(input("How many percentage of bill do you wanna give as a tip? 8, 10 or 12?")) / 100

total_bill_perperson = (bill / numof_friends) + ((bill / numof_friends) * tip)

# print(round(total_bill_perperson, 2))
print("{:.2f}".format(total_bill_perperson)) 
#using format instead of round
