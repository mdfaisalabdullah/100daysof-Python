
os.system("cls")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

chosen_cards_user = random.choices(cards, k=2)
chosen_cards_dealer = random.choices(cards, k=2)

run = True

while run == True:
    user_total = sum(chosen_cards_user)
    dealer_total = sum(chosen_cards_dealer)

    if user_total <= 21:
        print(f"Your cards: {chosen_cards_user}, current score: {user_total}")
        print(f"Dealer's first card: {chosen_cards_dealer[0]}")
        get_another = input("Type 'y' to get another card. Type 'n' to pass: ")

        if get_another == "y":
            chosen_cards_user.append(random.choice(cards))
            if dealer_total < 17:
                chosen_cards_dealer.append(random.choice(cards))
        else:
            run = False

    if user_total > 21:
        run = False

print(f"Your final hand {chosen_cards_user}, final score: {user_total}")
print(f"Dealer's final hand {chosen_cards_dealer}, final score: {dealer_total}")

user_distance = 21 - user_total
dealer_distance = 21 - dealer_total

if user_total > 21:
    print(f"You went over. You lose.")
elif dealer_total > 21:
    print(f"Dealer went over. Dealer lose.")
elif user_distance < dealer_distance:
    print(f"You won!!!")
elif dealer_distance < user_distance:
    print(f"oopss%%%....Dealer won!!")
elif dealer_distance == user_distance:
    print("You both score same!! The Game is DRAW.")
else:
    print("Something is wrong.Check code.")
