import random

WORD_LIST = ['forest', 'lime', 'putrid', 'olive', 'emerald', 'acid', 'sage']

def select_random_word(word_list):
    return random.choice(word_list)

def update_display_word(word, display_word, guess):
    return ''.join([guess if word[i] == guess else display_word[i] for i in range(len(word))])

def play_game():
    word = select_random_word(WORD_LIST)
    attempts = len(word) + 3
    display_word = '_' * len(word)
    guessed_letters = set()

    print("Welcome to Guess the Word!")
    print(f"The word has {len(word)} letters.")

    while attempts > 0 and display_word != word:
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            display_word = update_display_word(word, display_word, guess)
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts -= 1

    if display_word == word:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nOut of attempts! The word was: {word}")

if __name__ == "__main__":
    play_game()
