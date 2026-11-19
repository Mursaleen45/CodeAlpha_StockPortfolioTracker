import random

words = ["python", "computer", "program", "keyboard", "internet"]

word = random.choice(words)
guessed_letters = []
wrong_attempts = 0
max_attempts = 6

print("\n================================")
print("       WELCOME TO HANGMAN")
print("================================")
print("Guess the hidden word!")
print("You have 6 incorrect attempts.\n")

while wrong_attempts < max_attempts:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong attempts:", wrong_attempts)
    print("Remaining attempts:", max_attempts - wrong_attempts)

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word.")
        break

    guess = input("\nEnter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_attempts += 1
        print("Wrong guess!")

else:
    print("\nGame Over! You have used all your attempts.")
    print("The correct word was:", word)

print("\nThanks for playing Hangman!")