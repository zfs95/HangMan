import random
import sys


def display_hangman(lives):
    stages = [  # final state: head, torso, both arms, and both legs
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
    return stages[lives]


def dificulty():
    print("")
    print("\033[34mInstructions: \n")
    print("\033[37m1.\033[37m "+"\033[34mYou have to guess the word.")
    print("\033[37m2.\033[37m "+"\033[34mIf you enter a wrong letter you are going to lose a life.")
    print("\033[37m3.\033[37m "+"\033[34mIf you lose all your lives then you lose.")
    print("\033[37m4.\033[37m "+"\033[34mYou can only type one letter at a time.")
    print("\033[37m5.\033[37m "+"\033[34mIf you want to exit the game type "+"\'quit'.")
    print("\033[37m6.\033[37m "+"\033[34mType the dificulty you want to play on.\n")
    lvl_dificulty = input("Choose a dificulty from hard, medium or easy\033[37m: ")
    if lvl_dificulty == "hard":
        lives = 3
        return lives

    elif lvl_dificulty == "medium":
        lives = 4
        return lives
    elif lvl_dificulty == "easy":
        lives = 6
        return lives
    else:
        print("not a valid answer, try again")
        dificulty()


def get_word():
    random_word = ['TIRANA', 'ANDORRA LA VELLA', 'YEREVAN', 'VIENNA',
                   'BAKU', 'MINSK', 'BRUSSELS', 'SARAJEVO', 'SOFIA',
                   'ZAGREB', 'NICOSIA', 'PRAGUE', 'COPENHAGEN', 'TALLINN',
                   'HELSINKI', 'PARIS', 'TBILISI', 'BERLIN', 'ATHENS',
                   'BUDAPEST', 'REYKJAVIK', 'DUBLIN', 'ROME', 'NURSULTAN',
                   'PRISTINA', 'RIGA', 'VADUZ', 'VILNIUS', 'LUXEMBOURG',
                   'VALLETTA', 'CHISINAU', 'MONACO', 'PODGORICA', 'AMSTERDAM',
                   'SKOPJE', 'OSLO', 'WARSAW', 'LISBON', 'BUCHAREST', 'MOSCOW',
                   'SAN MARINO', 'BELGRADE', 'BRATISLAVA', 'LJUBLJANA', 'MADRID',
                   'STOCKHOLM', 'BERN', 'ANKARA', 'KYIV', 'LONDON', 'VATICANCITY']
    return random.choice(random_word)


def play_game():
    alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    word = get_word()
    letter_guessed = []
    lives = dificulty()
    guessed = False
    print(len(word) * " _ ")
    print(display_hangman(lives))
    while guessed is False and lives > 0:
        print("You have " + str(lives) + " lives left.")
        guess = input("Enter a letter: ").upper()
        # user inputs a letter
        if len(guess) == 1:
            if guess not in alphabet:
                print("You have not entered a letter")
                print(letter_guessed)
            elif guess in letter_guessed:
                print("You have already guessed that letter")
                print(letter_guessed)
                lives = lives
            elif guess not in word:
                print("\033[31mWrong!\033[37m Try again")
                letter_guessed.append(guess)
                print(letter_guessed)
                lives = lives-1
                print(display_hangman(lives))
            elif guess in word:
                print("\033[0;32mWell Done!\033[37m The letter is in the word")
                letter_guessed.append(guess)
                print(letter_guessed)
                print(display_hangman(lives))
        elif len(guess) > 1 and guess == "QUIT":
            sys.exit()
        elif len(guess) > 1 and guess != "QUIT":
            print("You can't enter more than 1 letter")
        status = ("")
        if guessed is False:
            for letter in word:
                if letter in letter_guessed:
                    status = status+letter
                else:
                    status = status + " _ "
            print(status)
        if status == word:
            print("\033[0;32mWell done\033[37m, you have guessed the word!")
            guessed = True
        elif lives == 0:
            print("\033[0;32mThe word was\033[37m: "+word)
            print("Game over. Try Again.")
    restart = input("Wanna try Again? yes/no ").lower()
    if restart == "yes":
        play_game()
    else:
        sys.exit(1)


play_game()
