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

versus = r'''                                                 
              .--.--.    
       ,---. /  /    '.  
      /__./||  :  /`. /  
 ,---.;  ; |;  |  |--`   
/___/ \  | ||  :  ;_     
\   ;  \ ' | \  \    `.  
 \   \  \: |  `----.   \ 
  ;   \  ' .  __ \  \  | 
   \   \   ' /  /`--'  / 
    \   `  ;'--'.     /  
     :   \ |  `--'---'   
      '---"                                     
'''

#Here its loaded all three options
choices = [rock, paper, scissors]


print("Welcome to the Rock Paper Scissors GAME!")
print("Píck one\n1-Rock\n2-Paper\n3-Scissors\n")

##Player input
human_choice = int(input("Pick one: "))
random_choice = random.randint(0,2)

##I changed it to make the comparisson easier (cause arrays starts at 0)
human_choice = human_choice -1

##validation to the player input
if human_choice < 0 or human_choice > 2:
    print("You had to pick a number between 1 to 3")
    exit()

if human_choice == random_choice:
    print("You:", choices[human_choice])
    print(versus)
    print("Enemy:", choices[random_choice])
    print("\nDRAW!")

elif human_choice == 0 and random_choice == 2:
    print("You:", choices[human_choice])
    print(versus)
    print("Enemy:", choices[random_choice])
    print("\nYou WIN!")

elif human_choice == 1 and random_choice == 0:
    print("You:", choices[human_choice])
    print(versus)
    print("Enemy:", choices[random_choice])
    print("\nYou WIN !")

elif human_choice == 2 and random_choice == 1:
    print("You:", choices[human_choice])
    print(versus)
    print("Enemy:", choices[random_choice])
    print("\nYou WIN!")

else:
    print("You:", choices[human_choice])
    print(versus)
    print("Enemy:", choices[random_choice])
    print("\nYou LOSE!")








