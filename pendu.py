"""
HangMixone v3 :
- Functions defined.
- Docstrings added.
- Use of main().
- PEP8 is respected.
- More user friendly.
- List of words and way of implementing said list can still be improved upon.
- (NEW) Instead of opening file, words of same length now printed.
- (NEW) Name inclusion properly done (only aesthetic).
- (NEW) Wrong guesses improvement print.
- (NEW) Improved timing and prints for guesses.
"""

__author__ = "Miguel Terol Espino"
__date__ = "02 December 2014"
__version__ = "HangMixone v3.4.4"

from time import sleep
from random import choice


def print_state(guesses, word, guessesbad):
    """
    Prints either _ or the character depending on if it has been guessed or not.
    :param guesses: list containing guesses made for printing
    :param word: secret word
    :param guessesbad: lists containing guesses not in word to show to user
    :return: returns the number of characters not correctly guessed at a certain point in time
    """
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" "),
            failed += 1
    if len(guessesbad) > 1:
        print("\n\nWrong guesses :", guessesbad)
    return failed


def welcome():
    """
    Welcomes the user and prepares initial input of lives.
    :return: number of lives
    """
    print("\nWelcome human.")
    sleep(0.2)
    name = input("What shall I address you as ? : ")
    sleep(0.2)
    print("\nHello, " + name, "\nTime to play HangMixone !\n")
    lives = 0
    while lives <= 0:
        try:
            lives = int(input("How many lives shall you dispose of ? : "))
            if lives <= 0:
                print("Your number of lives can't be 0 or negative foolish human !")
        except ValueError:
            print("\nThat was not a valid input !\n")
    return lives, name


def main():
    """
    Initiates hangman program.
    Functions used: - print_state(guesses, word, guessesbad) => Prints secret word, either hidden or revealed
                    -welcome() => Initial welcome and initial parameters like name and lives are defined
    :return: None
    """
    data = welcome()
    lives = data[0]
    name = data[1]
    inputfile = open("mywords.txt")
    words = inputfile.readlines()
    word = choice(words)[:-1]
    inputfile.close()
    guesses = ""
    guessesbad = ""
    print("\nStart guessing in \n3"), sleep(0.5), print("2"), sleep(0.5), print("1\n")
    sleep(0.5)
    won = False
    while lives > 0 and not won:
        sleep(0.2)
        failed = print_state(guesses, word, guessesbad)
        if failed == 0:
            print("\nYou won !")
            won = True
        guess = input("\nGuess a letter: ")
        if guess == "help":
            sleep(0.2)
            print("In exchange for one life," +
                  "\nyou may view the words of the same length from amongst those possibly chosen.")
            sleep(0.3)
            input("Press enter to forsake one life and view the file {0} ...\n".format(name))
            for palabra in words:
                if len(palabra) == len(word) + 1:
                    print(palabra)
                    sleep(0.2)
            sleep(0.3)
            lives -= 1
        elif guess == word:
            print("\nYou guessed the word correctly ! \nCongratulations", name, "you won !")
            won = True
        elif len(guess) < 2:
            guesses += guess
        else:
            guesses += guess[0]
            print("Entry should be only one letter long, \nonly first letter of '"+guess+"' will be accepted.")
        if (guess not in word) and (guess != "help"):
            guessesbad += guess + " "
            lives -= 1
            sleep(0.5)
            print("\nWrong", "\a")
        if won:
                print("You ended the game with", lives, "lives!\n")
        elif lives != 0:
            print("\nYou have",  lives, "lives left\n")
        else:
            print("\nYou loose", name, "!\nThe word was '"+word+"'.\n")

if __name__ == "__main__":
    main()

