import random
from posixpath import commonpath

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

opt = [rock, paper, scissors]

userinput = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

userinput = int(userinput)
print("User:\n"+ opt[userinput])

computerinput = random.randint(0, 2)
print("Computer:\n" + opt[computerinput])

if userinput == 0 and computerinput == 2:
    print("You chose rock. Computer chose scissors. You won over computer.")
elif userinput == 2 and computerinput == 0:
    print("You chose scissors. Computer chose rock. You lost.")
elif userinput == 2 and computerinput == 1:
    print("You chose scissors. Computer chose paper. You won over computer.")
elif userinput == 1 and computerinput == 2:
    print("You chose paper. Computer chose scissors. You lost.")
elif userinput == 1 and computerinput == 0:
    print("You chose paper. Computer chose rock. You won over computer.")
elif userinput == 0 and computerinput == 1:
    print("You chose rock. Computer chose paper. You lost.")
else:
    print("The Game is draw. You both win!!!")
