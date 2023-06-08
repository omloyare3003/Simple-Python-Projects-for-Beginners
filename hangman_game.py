import random

def select_word():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grapefruit", "honeydew"]
    return random.choice(word_list)

def display_word(word, guesses):
    displayed_word = ""
    for letter in word:
        if letter in guesses:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    attempts = 6
    guessed_letters = []
    word = select_word()

    print("Welcome to Hangman!")
    print("Guess the letters to uncover the word.")

    while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Guessed letters:", guessed_letters)
        print("Word:", display_word(word, guessed_letters))

        guess = input("Enter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word:
                guessed_letters.append(guess)
                if set(word) == set(guessed_letters):
                    print("Congratulations! You guessed the word:", word)
                    break
            else:
                print("Wrong guess!")
                attempts -= 1
                if attempts == 0:
                    print("Game over! The word was:", word)
        else:
            print("Invalid input. Please enter a single letter.")

if __name__ == '__main__':
    hangman()
