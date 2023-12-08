print("The Love Calculator is calculating your score...")
name1 = input("What is your name? : ")  # What is your name?
name2 = input("What is their name? : ")  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name_combined = name1 + name2

name_lower = name_combined.lower()

t = name_lower.count("t")
r = name_lower.count("r")
u = name_lower.count("u")
e = name_lower.count("e")

first_digit = str(t + r + u + e)

l = name_lower.count("l")
o = name_lower.count("o")
v = name_lower.count("v")
e = name_lower.count("e")

second_digit = str(l + o + v + e)

digit_combined = first_digit + second_digit

int_digit_combined = int(digit_combined)

if int_digit_combined <= 10 or int_digit_combined >= 90:
    print(f"Your score is {
          int_digit_combined}, you go together like coke and mentos.")

elif int_digit_combined >= 40 and int_digit_combined <= 50:
    print(f"Your score is {int_digit_combined}, you are alright together.")

else:
    print(f"Your score is {int_digit_combined}.")
