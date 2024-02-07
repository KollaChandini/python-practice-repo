import random
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
game_images = [rock, paper, scissors]
print("Welcome to Rock, Paper, Scissors game!")
user_choice = int(input("What do you want to choose? Enter 0 for Rock, 1 for Paper and 2 for Scissors: "))

if user_choice > 2 or user_choice < 0:
    print("Invalid input.")
else:
    print(game_images[user_choice])
    computers_choice = random.choice(0, 2)
    print("Computer chose:")
    print(game_images[computers_choice])
    if user_choice == 0 and computers_choice == 1:
        print("You win.")
    elif user_choice == 2 and computers_choice == 1:
        print("You win.")
    elif user_choice == 0 and computers_choice == 2:
        print("You win.")
    elif user_choice == computers_choice:
        print("It's a draw.")
    else:
        print("Computer win.")
    















