import random
from game_data import data_list

# format account data into printable format
def format_function(account):
    ''' take account dara and return pritable format '''
    return f" {account['name']}, {account['description']}, from {account['country']}."

def check_answer(user_guess,a_follower_count,b_follower_count):
    ''' take user guess and followers count and return if they got right '''
    if a_follower_count>b_follower_count :
        return user_guess=="a"
    else:
        return user_guess=="b"


score=0
game_should_continue=True
account_b=random.choice(data_list)
while game_should_continue:
    # generate random account from the game_data
    account_a=account_b
    account_b=random.choice(data_list)
    if account_a==account_b:
        account_b = random.choice(data_list)
    print(f"compare A:{format_function(account_a)}")
    print("\nVS\n")
    print(f"compare B:{format_function(account_b)}")

    # ask user to guess
    user_guess=input("Who has more followers? Type 'A' or 'B':").lower()

    # check if user is correct
    # collect follower count
    a_follower_count = account_a["followers"]
    b_follower_count = account_b["followers"]

    is_correct=check_answer(user_guess,a_follower_count,b_follower_count)
    #give feed back to user
    if is_correct:
        score+=1
        print(f"You are right! current score is {score}\n")

    else:
        print(f"You are wrong , final score {score}\n")
        game_should_continue=False





