import guess_the_word
import pytest

def test_select_random_word():
    for _ in range(10):
        word = guess_the_word.select_random_word(guess_the_word.WORD_LIST)
        assert word in guess_the_word.WORD_LIST

def test_update_display_word_correct_guess():
    word = "forest"
    display_word = "______"
    guess = "o"
    updated = guess_the_word.update_display_word(word, display_word, guess)
    assert updated == "_o____"

def test_update_display_word_incorrect_guess():
    word = "forest"
    display_word = "______"
    guess = "z"
    updated = guess_the_word.update_display_word(word, display_word, guess)
    assert updated == "______"

def test_update_display_word_multiple_correct_guesses():
    word = "emerald"
    display_word = "_______"
    guess = "e"
    updated = guess_the_word.update_display_word(word, display_word, guess)
    assert updated == "e_____d" or updated.count("e") == word.count("e")  # e appears twice
