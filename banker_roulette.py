import random

names = input("이름을 입력해주세요 : ").split(", ")

num_names = len(names)

names_random_as_int = random.randint(0, num_names - 1)

names_as_str = names[names_random_as_int]

print("[+] " + names_as_str + " 이(가) 당첨되었습니다. 축하합니다 당신이 오늘 밥을 살 수 있게 되었습니다! [+]")

# or 아래와 같은 방식으로도 가능 똑같이 가능하다.
# choice() function 이용함으로써.

# name_selected = random.choice(names)

# print("[+] " + name_selected + " 이(가) 당첨되었습니다. 축하합니다 당신이 오늘 밥을 살 수 있게 되었습니다! [+]")
