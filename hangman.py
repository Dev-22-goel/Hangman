import random

# used for getting some words from a list
from words import word_list


def main():

    word = get_word()
    play(word)

    # depends if user wants to play the game.
    while input("Want to Play Again? (Y/N) ") == "Y":
        word = get_word()
        play(word)


def get_word():
    # choose any random word
    word = random.choice(word_list)

    # keeping the letters as uppercase to reduce confusion
    return word.upper()


def play(word):
    # underscores/blanks
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []

    # Max no. of wrong guess for a user
    lives = 6

    print("\nLet's play Hangman!")

    # will display the initial stage of the hangman
    print(display_hangman(lives))

    # will display how many words/letters were guessed
    print(word_completion)
    print("\n")

    # loop will continue till word is not guessed and the number of tries left
    while not guessed and lives > 0:

        # casting user input as upper
        guess = input("Please guess a letter or word: ").upper()

        # if guessing an alphabet only
        if len(guess) == 1 and guess.isalpha():

            # if letter was already guessed
            if guess in guessed_letters:
                print("You already guessed the letter", guess)

            # if letter is not matching
            elif guess not in word:
                print(guess, "is not in the word.")

                # remembering the trials
                lives -= 1

                # adding the non-matched letter to the list
                guessed_letters.append(guess)

            # if the letter is guessed and matches
            else:
                print("Good job,", guess, "is in the word!")

                # adding the matched letter to the list
                guessed_letters.append(guess)

                # converting the string to a list, makes easier to access different letters
                word_as_list = list(word_completion)

                # enums help the user to get the index number and letters consecutively
                indices = [x for x, letter in enumerate(word) if letter == guess]

                for index in indices:
                    # replacing each underscore with the letter
                    word_as_list[index] = guess

                # converting a list to string
                word_completion = "".join(word_as_list)

                # checking for blank spaces
                if "_" not in word_completion:
                    guessed = True

        # case where the user inputs the word
        elif len(guess) == len(word) and guess.isalpha():

            if guess in guessed_words:
                print("You already guessed the word", guess)

            elif guess != word:
                print(guess, "is not the word.")
                lives -= 1
                guessed_words.append(guess)

            else:
                guessed = True
                word_completion = word

        # all other (false) cases
        else:
            print("Not a valid guess.")

        # after each guess we need to provide the user with the status of the game
        print(display_hangman(lives))
        print(word_completion)
        print("\n")

    # means if guessed is True
    if guessed:
        print("Congrats, you guessed the word! You win!")

    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # initial and final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


main()
