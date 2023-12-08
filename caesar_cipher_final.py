from caesar_cipher_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"

    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
print(logo)
# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).
    shift = shift % 26
# while shift > 26 or shift < 0:
#     print("0 ~ 26사이의 범위를 입력해주세요.")
#     shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("프로그램을 다시 시작하시겠습니까? Type Yes' or 'No' :\n").lower()
    if result == "no":
        should_continue = False
        print("Good Bye")
    elif result == "yes":
        should_continue = True
        # 여러번 else: 일 경우, 즉 여러번 '예' '아니요'가 아닌 다른 글자를 입력했을 때는 계속 다시 입력하라는 인풋창이 나오도록 만듥 것. 한번만이 아닌.
    else:
        result = input("'Yes' or 'No'로 다시 입력해주세요. :\n")
