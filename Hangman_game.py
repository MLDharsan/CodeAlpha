import random

# List of words for the game
word_list = ['python', 'hangman', 'programming', 'developer', 'computer','codealpha']


def get_random_word():
    return random.choice(word_list).upper()


def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()


def display_status(attempts_left, max_attempts):

    filled = '█' * attempts_left
    empty = '░' * (max_attempts - attempts_left)
    progress_bar = filled + empty


    if attempts_left == max_attempts:
        status = "PERFECT - Keep going!"
    elif attempts_left >= 4:
        status = "GOOD - You're doing well!"
    elif attempts_left >= 2:
        status = "CAREFUL - Running out of attempts!"
    else:
        status = "DANGER - Last chance!"

    print("\n" + "=" * 50)
    print(f"Lives: {progress_bar} [{attempts_left}/{max_attempts}]")
    print(status)
    print("=" * 50)


def play_hangman():
    """Main function"""
    print("\n" + "=" * 50)
    print(" WELCOME TO HANGMAN GAME! ")
    print("=" * 50)
    print("Guess the word one letter at a time.")
    print("You have 6 incorrect guesses allowed.")

    # Initialize game variables
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6

    # Game loop
    while incorrect_guesses < max_attempts:
        # Display current state
        display_status(max_attempts - incorrect_guesses, max_attempts)

        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        # Check if player won
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 50)
            print("CONGRATULATIONS! YOU WON! ")
            print(f"The word was: {word}")
            print("=" * 50)
            return

        # Get player input
        guess = input("\n Enter a letter: ").upper()

        # Validate input
        if len(guess) != 1:
            print(" Please enter only one letter!")
            continue

        if not guess.isalpha():
            print(" Please enter a valid letter!")
            continue

        if guess in guessed_letters:
            print("  You already guessed that letter!")
            continue

        # Add guess to guessed letters
        guessed_letters.add(guess)

        # Check if guess is correct
        if guess in word:
            print(f" Correct! '{guess}' is in the word!")
        else:
            incorrect_guesses += 1
            print(f" Wrong! '{guess}' is not in the word.")
            print(f"Mistakes: {incorrect_guesses}/{max_attempts}")

    # Game over - player lost
    display_status(0, max_attempts)
    print("\n" + "=" * 50)
    print(" GAME OVER! YOU LOST! ")
    print(f"The word was: {word}")
    print("=" * 50)


def main():
    """Main function to run the game"""
    while True:
        play_hangman()

        # Ask to play again
        play_again = input("\n Do you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\n Thanks for playing! Goodbye!")
            break
        print("\n" * 2)


if __name__ == "__main__":
    main()