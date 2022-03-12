## hangman game project

#Step 1 

import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = word_list[random.randint(0, len(word_list) - 1)]

# or random.choice(word_list)

print("A random word has been generated.")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter of that word:").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for ltr in chosen_word:
    if ltr == guess:
        print("right")
    else:
        print("wrong")

print("chosen word is: " + chosen_word)
