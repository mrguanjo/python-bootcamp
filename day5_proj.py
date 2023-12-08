import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_list = []

for i in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for i in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for i in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password_as_string = ""
for i in password_list:
    password_as_string += i

print(f"Your password is: {password_as_string}")

# or

# length_of_string = nr_letters + nr_symbols + nr_numbers

# letters_random = random.sample(letters, nr_letters)
# symbols_random = random.sample(symbols, nr_symbols)
# numbers_random = random.sample(numbers, nr_numbers)

# sum_of_letters = ''.join(letters_random)
# sum_of_symbols = ''.join(symbols_random)
# sum_of_numbers = ''.join(numbers_random)

# letters_as_string = sum_of_letters + sum_of_symbols + sum_of_numbers

# letters_randomly = ''.join(random.sample(
#     letters_as_string, length_of_string))
# print("Your password is: " + letters_randomly)
