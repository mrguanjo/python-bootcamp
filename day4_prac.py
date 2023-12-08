# import random

# 0.0000... ~ 4.99999 까지의 난수 만들기
# random_inter = random.randint(1, 4)
# random_float = random.random()
# print(random_inter + random_float)

# or

# print(random_float * 5)

# import my_module

# print(my_module.speed_of_light)

# states_of_the_america = ["Delaware", " Pennsylvania"]

# states_of_the_america.append(
#     "New Jersey")

# states_of_the_america.extend(["Georgia", " Connecticut", "Massachusetts"])

# print(states_of_the_america)

# fruits = ["Bluberries", "Banana", "Strawberries"]

# vegetables = ["Tomatoes", "potatoes"]

# sets_of_list_data = [fruits, vegetables]

# print(sets_of_list_data)

fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

# 첫번째 리스트의 3번째 데이터를 불러오라는 명령어.
print(dirty_dozen[0][2])
