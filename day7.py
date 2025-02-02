import random
print("welcome to the hangman game")
world_list=['camell','cat','horse']
chosen_word=random.choice(world_list)
placeholder=""
for i in range(len(chosen_word)):
    placeholder+='_ '  # 3 * _ for cat
print(placeholder)

game_over=False
lives=6
correct_letter=[]
while(game_over is False and lives > 0):
    user_input=input("guess a letter").lower()
    display = ""
    if user_input in correct_letter:
        print(f"already guess the letter {user_input}")
    for letter in chosen_word:
        if letter == user_input:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display+=letter
        else:
            display += " _ "
    if user_input not in chosen_word:
        lives -= 1
        print("attempts left for user to guess ",lives)
        if lives ==0:
            print("You Loose")
    print(display)
    if "_" not in display:
        game_over=True
        print("you guess it correctly ")


