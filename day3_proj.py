print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/____/___
*******************************************************************************
''')

print("[+] Welcome to Treasure Island.\n[+] Your mission is to find the treasure.\n[+] Good Luck!!!")

direction = input(
    "당신은 지금 갈림길에 서 있습니다. 어느 방향으로 가시겠습니까? Please Type 'Left' or 'Right'\n>>> ").lower()

# act = input(
#     "보물을 찾기위해 숲 속으로 들어가실건가요? 아니면 현재 위치에서 기다리면서 상황을 지켜보시겠습니까? Forest or wait").lower()

# choose = input(
#     "기다리다보니 갑자기 눈 앞에 3개의 서로 다른 색을 가진 문이 나타났습니다. 세개의 문 중 어느 문으로 들어가시겠습니까? Red, Green or Blue").lower()

if direction == "left":
    print("*** Wow! You are survive! Congratuaion!!! *** ")
    act = input(
        "다시 한번 선택의 순간이 왔습니다. 당신은 보물을 찾기위해 숲 속으로 들어가실건가요? 아니면 현재 위치에서 기다리면서 상황을 지켜보시겠습니까? Please Type 'Forest' or 'Wait'\n>>> ").lower()
    if act == "wait":
        print("*** 인내심을 가진 당신, 살아남았습니다. 축하드립니다!!! ***")
        choice = input(
            "인내를 가지고 기다리다보니 당신 눈 앞에 갑자기 3개의 서로 다른 색을 가진 문이 나타났습니다. 세개의 문 중 어느 문으로 들어가시겠습니까? Please Type 'Red', 'Green' or 'Blue'\n>>> ").lower()
        if choice == "green":
            print("[+] You found a Treasure! Congratuation!!! [+]")
        elif choice == "red":
            print("빨간문에 들어간 당신, 한순간 온 몸이 화염에 뒤덮여 사망하였습니다.\n[+] Game Over ㅠ_ㅠ")
        else:
            print(
                "파란문에 들어간 당신, 바로 눈 앞에 커다란 북극곰이 나타나 당신을 공격하여 사망하였습니다.\n[+] Game Over ㅠ_ㅠ ")
    else:
        print("당신은 숲 속에서 맹수를 만나 공격을 당해 사망하였습니다.\n[+] Game Over ㅠ_ㅠ")
else:
    print("당신은 낭떠러지에 떨어졌습니다.\n[+] Game Over ㅠ_ㅠ")