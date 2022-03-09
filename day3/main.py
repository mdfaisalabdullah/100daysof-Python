# print("Welcome to the first child theme park.")
# age = int(input("What is your age?"))

# if age < 18:
#     print("You can enter the theme park.")

# elif age < 40:
#     role = input("What is your role with the little person?Mother? Father? ")

#     if role == "Mother":
#         print("You can enter the theme park as a parent.")
#     elif role == "Father":
#         print("You can enter the theme park as a parent.")
#     else:
#         print("You can not enter the theme park bcz you have not the authority over the child.")
    
# else:
#     print("Sorry. You can not enter the theme park.")

print("Welcome to the first child theme park.")
bill = 5
height = int(input("What is your height?"))

if height > 120: 
    print("You can ride.")
    age = int(input("What is your age?"))
    if age < 12:
        bill += 5
    elif age < 18:
        bill += 7
    else:
        bill += 12
    
    photo = input("Do you wanna take photo? yes or no?")

    if(photo == "yes"):
        bill += 3
    
    print(f"Your total bill is {bill}.")
else:
    print("You can not ride.")


#Exercise: odd or even,pizza shop bill , theme park bill, love score calculator.
