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
import random
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choice= random.randint(0,2)

if user_choice==0:
    print(rock)
    if computer_choice==0:
      print(rock)
      print("Draw")
    elif computer_choice==1:
      print(paper)
      print("You lost")
    elif computer_choice==2:
      print(scissors)
      print("You won")
elif user_choice==1:
    print(paper)
    if computer_choice==0:
      print(rock)
      print("You won")
    elif computer_choice==1:
      print(paper)
      print("Draw")
    elif computer_choice==2:
      print(scissors)
      print("You lost")
elif user_choice==2:
    print(scissors)
    if computer_choice==0:
      print(rock)
      print("You lost")
    elif computer_choice==1:
      print(paper)
      print("You won")
    elif computer_choice==2:
      print(scissors)
      print("Draw")

print("Happy playing! ")