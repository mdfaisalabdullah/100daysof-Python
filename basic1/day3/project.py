
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

leftright = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'.")

if leftright == 'left':
    print("You come to a lake. There is an island in the middle of the lake.")
    waitswim = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if waitswim == 'wait':
        door = input("Which door do you wanna go in? red, blue or yellow? please select carefully.")
        if door == 'red':
            print("Burnt by fire. Game Over.")
        elif door == 'blue':
            print("Eaten by beast. Game Over.")
        elif door == 'yellow':
            print("Congrats! You have WON! Let's have party!!!!!!!!!!!!!")
        else:
            print("Game Over.")
    else:
        print("You are attacked by trout. Game Over.")
else:
    print("You are fall into a hole. Game Over.")
