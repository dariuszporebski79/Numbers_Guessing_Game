from random import randint
computer_number = randint(1, 100)
while True:
    player_number = int(input("Guess the number: "))
    if player_number < computer_number:
        print("Too small!")
    elif player_number > computer_number:
        print("Too big!")
    else:
        print("You win")
        break
# ValueError
