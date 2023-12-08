import random

computer_choice = random.randint(0, 2)

try:
    my_choice = int(
        input("가위를 선택하시려면 '2'를, 바위를 선택하시려면 '0'을, 보를 선택하시려면 '1'을 적어주세요. :  "))
except:
    print("잘못된 입력입니다. 숫자로 입력해주세요.")
    exit()


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

if my_choice >= 3 or my_choice < 0:
    print("잘못된 숫자입니다. 0과 2사이의 숫자를 입력해주세요.")
else:
    print(game_images[my_choice])
    print("Computer Chose : ")
    print(game_images[computer_choice])

    if my_choice == 2 and computer_choice == 1:
        print("당신이 이겼습니다.")
    elif my_choice == 2 and computer_choice == 0:
        print("당신이 졌습니다.")
    elif my_choice == 1 and computer_choice == 0:
        print("당신이 이겼습니다.")
    elif my_choice == 1 and computer_choice == 2:
        print("당신이 졌습니다.")
    elif my_choice == 0 and computer_choice == 2:
        print("당신이 이겼습니다.")
    elif my_choice == 0 and computer_choice == 1:
        print("당신이 졌습니다.")
    elif my_choice == computer_choice:
        print("비겼습니다.")
