## function return
## calculator app
import art


def add(num1, num2):
    return num1 + num2


def substriction(num1, num2):
    return num1 - num2


def multiple(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


operations = {"+": add, "-": substriction, "*": multiple, "/": division}


def calculator():
    print(art.logo)
    print("Do a new calculation.")

    first_number = float(input("What is the first number? : "))

    for symb in operations:
        print(symb)

    continue_calc = True

    while continue_calc:

        operation_symb = input("Pick an operation: ")
        next_number = float(input("What is the next number? : "))
        calculate = operations[operation_symb]
        answer = calculate(first_number, next_number)

        print(f"{first_number} {operation_symb} {next_number} = {answer}")

        do_continue = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: "
        )

        if do_continue == "n":
            continue_calc = False
            calculator()
        elif do_continue == "y":
            first_number = answer
        else:
            continue_calc = False
            calculator()


calculator()


#
#
#
##
#
#
#######################
# value = 0

# if operation == "+":
#     value = add(first_number, next_number)
# elif operation == "-":
#     value = substriction(first_number, next_number)
# elif operation == "*":
#     value = multiple(first_number, next_number)
# elif operation == "/":
#     value = division(first_number, next_number)
# else:
#     print("Enter correct operation.")

# print(value)
