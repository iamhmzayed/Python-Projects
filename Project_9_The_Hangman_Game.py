#Project_9_The_Hangman_Game

import random


def hangman():
    # List of possible words
    words = ['python', 'java', 'kotlin', 'javascript', 'hangman', 'programming']

    # Randomly select a word
    word = random.choice(words)
    word_letters = set(word)  # unique letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  # letters guessed by the user

    lives = 6  # Number of attempts
    a = input("What is your name ? ")
    print(f"Welcome {a} .  Let's Play Hangman!")
    print("......................................")
    print(f"The word has {len(word)} letters.")
    print("_ " * len(word))

    # Main game loop
    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left and you have used these letters: {' '.join(used_letters)}")

        # Display current state of the word
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))

        # Get user input
        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives -= 1
                print(f"\nYour letter, {user_letter}, is not in the word.")
        elif user_letter in used_letters:
            print("\nYou have already used that letter. Try again.")
        else:
            print("\nInvalid character. Please enter a letter from the alphabet.")

    if lives == 0:
        print("\nYou died, sorry. The word was", word)
    else:
        print("\nCongratulations! You guessed the word", word, "!!")


hangman()
