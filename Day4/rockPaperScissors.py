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

gameImg = [rock, paper, scissors]

# Player logic
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print("You choose: ")
print(gameImg[player])

# PC Logic
pc = random.randint(0, 2)
print("Computer choose: ")
print(gameImg[pc])

if player >= 3 or player < 0:
    print("You typed an invalid number. You lose!")
elif player == 0 and pc == 2:
    print("You win!")
elif pc == 0 and player == 2:
    print("You lose!")
elif pc > player:
    print("You lose!")
elif player > pc:
    print("You win!")
elif pc == player:
    print("Draw!")



