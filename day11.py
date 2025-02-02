import random
def deal_card():
    # return random card form the cards deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    c = random.choice(cards)
    return c
def calculate_score(cards):
    #   take a list cards and return score calculated from the cards
    if sum(cards) == 21 and len(cards) == 2:  # this is for 2 cards and 21 sum then declare blackjack
        return 0
    if sum(cards) > 21 and 11 in cards:  # this is case for the ace and return sum
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "loss,opponent has Blackjack"
    elif u_score == 0:
        return "you win with the blackjack"
    elif u_score > 21:
        return "you went over,you loose"
    elif c_score > 21:
        return "opponent went over,you win"
    elif u_score > c_score:
        return "you win"
    else:
        return "you loose"
def play_game():
    user_card = []
    computer_card = []
    computer_score = -1
    is_game_over = False
    for _ in range(1):
        user_card.append(deal_card())  # [8,9]
        computer_card.append(deal_card())  # [4,2]
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"your card {user_card},current score is {user_score}")
        print(f"computer first card is  {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type y to get another card,type n to pass")
            if user_should_deal == 'y':
                user_card.append(deal_card())
            elif user_should_deal == 'n':
                is_game_over = True
            else:
                print("invalid input")
        while computer_score != 0 and computer_score < 17:
            computer_card.append(deal_card())
            computer_score = calculate_score(computer_card)
    print(f"your final hand {user_card} and score {user_score}")
    print(f"computer final hand {computer_card} and {computer_score}")
    print(compare(user_score, computer_score))
while input("do you want to play a game of blackjack? type y or n") == 'y':
    print("\n")
    play_game()