import random
from hangman_word_list import word_list
from hangman_asci import logo, stages

print(f"Welcome to hangman\n{logo}")
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)

display = []
for _ in range(word_length):
    display += '_'

game_is_on = True
life = 6

while game_is_on:
    print(stages[life])
    print(display)
    guess = input("Guess a letter:")
    if guess in display:
        print(f"You already guessed this letter: {guess}")
    for position in range(word_length):
        if guess == chosen_word[position]:
            display[position] = guess
            print("Correct!")
    if guess not in chosen_word:
        life -= 1
        print("Wrong you lose a life")
    if '_' not in display:
        print(display)
        game_is_on = False
        print("You Win")
    if life < 0:
        game_is_on = False
        print("You lose")