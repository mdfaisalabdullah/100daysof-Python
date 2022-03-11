##
#loop
#for loop

# fruits = ["apple", "mango", "banana"]

# for fruit in fruits:
#     print(fruit + " Pie")


#

##ex calculate average of the age given in a list
## using for loop

# ages = [23, 25, 11, 24, 44]

# total = 0
# num_of_students = 0

# for age in ages:
#     total += age

# for num in ages:
#     num_of_students += 1

# print(total / num_of_students )


# using function(build in)

# totals = sum(ages)

# nums = len(ages)

# print(totals/nums)

##
#################
#ex. get highest score in a list

# scores = [34, 55, 67, 85, 99, 35]

# highest_score = 0
# lowest_score = 100

# for score in scores:
#     if score > highest_score:
#         highest_score = score
#     if score < lowest_score:
#         lowest_score = score

# print(f"highest score is: {highest_score} \n lowest score is: {lowest_score}")


## for loop for any range

# total = 0
# for number in range(1, 101):
#     total += number

# print(total)

## sum of even number till 100

# even_total = 0
# for even in range(2,101, 2):
#     even_total += even

# print(even_total)


####################
## FizzBuzz Exercise:

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("Fizz Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
