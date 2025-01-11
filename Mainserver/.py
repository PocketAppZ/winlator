
```
import random

choices = ['rock', 'paper', 'scissors']

def game():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)

    print(f"\nUser: {user_choice}")
    print(f"Computer: {computer_choice}\n")

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

game()
```

