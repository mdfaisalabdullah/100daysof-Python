#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


## thought process
# if user tell how many letters - then each time it will select random letter from the letters
#same will go for numbers and symbols

# concat all of them 
#final ouput

#############easy way

# lengthltr = len(letters)
# lengthnum = len(numbers)
# lengthsymb = len(symbols)

# password = ""

# for ltr in range(1, nr_letters + 1):
#     randomltr = letters[random.randint(0, lengthltr-1)]
#     password += randomltr

# for ltr in range(1, nr_numbers + 1):
#     randomnum = numbers[random.randint(0, lengthnum-1)]
#     password += randomnum

# for symb in range(1, nr_symbols + 1):
#     random_symb = symbols[random.randint(0, lengthsymb-1)]
#     password += random_symb

# print(password)

###
#########
##
#
# hard level
#####
#



# lengthltr = len(letters)
# lengthnum = len(numbers)
# lengthsymb = len(symbols)

# password = []


# for ltr in range(1, nr_letters + 1):
#     randomltr = letters[random.randint(0, lengthltr-1)]
#     password.append(randomltr)

# for ltr in range(1, nr_numbers + 1):
#     passwordlength = len(password)
#     randomnum = numbers[random.randint(0, lengthnum-1)]
#     password.insert(random.randint(0, passwordlength - 1), randomnum)

# for symb in range(1, nr_symbols + 1):
#     passwordlength = len(password)
#     random_symb = symbols[random.randint(0, lengthsymb-1)]
#     password.insert(random.randint(0, passwordlength - 1), random_symb)

# print(password)
# print(''.join(password))

#####
#
#
#

## hard level alternative solution

password = []

for char in range(1, nr_letters + 1):
    # password.append(random.choice(letters))
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)


for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)

random.shuffle(password)
print(password)

final_password = ""

for char in password:
    final_password += char

print(final_password)
