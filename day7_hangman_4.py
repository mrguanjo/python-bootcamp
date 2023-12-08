# Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1  # for문 안에 if문을 넣으면 6글자 중 5글자가 맞지 않으면 한번에 5개의 목숨이 깎임.
        if lives == 0:
            end_of_game = True
            print("You Lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])


# "baboon"이 정답이면, b를 처음입력할 때는 잘 작동하나, 두번째로 중복되면, 라이프가 차감되어야 하는데, 그렇지 않고, 계속 무한 루프에 갖힌다.
# 또한, if not letter == guess: 를 for문 밖에 입력해도, 정답을 맞혀도 라이프가 차감되는 문제를 해결해야 함. 즉 if guess not in chosen_word: 와 무엇이 다른지에 대한 이해가 필요.
