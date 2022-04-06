from PyDictionary import PyDictionary
from numpy import number
dictionary = PyDictionary()

correct_word = "champion".lower()
number_of_guesses = 7
list_of_letters = []

for letter in correct_word:
    list_of_letters.append("_")

print(' '.join(list_of_letters), end = "\n\n" )


def Guess_Choice():
    guess_choice = input('Do you want to guess a letter or a word?: ')
    print()
    valid_choice = False

    while (valid_choice == False):
        if guess_choice.lower() == "word":
            valid_choice = True
            guess_choice = 0
        elif guess_choice.lower() == "letter":
            valid_choice = True
            guess_choice = 1
        else:
            guess_choice = input('Invalid input. Do you want to guess a letter or a word?: ')
            print()
    return guess_choice


def Validate_Guess(choice):
    
    global number_of_guesses
    global correct_word
    global list_of_letters

    if choice == 0:
        guess = input("Guess a word: ").lower()
        print()
        valid_word = bool(dictionary.meaning(guess, True))
        while valid_word == False:
            guess = input("Invalid input. Guess a word: ").lower()
            print()
            valid_word = bool(dictionary.meaning(guess,True))
        if guess == correct_word:
            list_of_letters = list(correct_word)
            print("You win!\n")
            print("The word was \n")
            number_of_guesses = 0
        else:
            print("Incorrect! You lose a guess!\n")
            number_of_guesses = number_of_guesses - 1
            if number_of_guesses > 1:
                print(f'You have {number_of_guesses} guesses left.\n')
            elif number_of_guesses == 1:
                print(f'You have {number_of_guesses} guess left. Make it count!\n')
            else:
                list_of_letters = list(correct_word)
                print("You are out of guesses! You lose!\n")
                print(f"The word was \n")
    else:
        guess = input("Guess a letter: ").lower()
        print()
        valid_letter = guess.isalpha()
        while (valid_letter == False or len(guess) != 1) :
            guess = input("Invalid input. Guess a letter: ").lower()
            print()
            valid_letter = guess.isalpha()
        if any(letter in correct_word for letter in guess):
            print("Correct!\n")
            for i in range(0,len(correct_word)):
                if guess == list(correct_word)[i]:
                    list_of_letters[i] = guess
        else:
            print("Incorrect! You lose a guess! \n")
            number_of_guesses = number_of_guesses - 1
            if number_of_guesses > 1:
                print(f'You have {number_of_guesses} guesses left.\n')
            elif number_of_guesses == 1:
                print(f'You have {number_of_guesses} guess left. Make it count!\n')
            else:
                print("You are out of guesses! You lose!\n")
                print(f"The word was \n")
                list_of_letters = list(correct_word)
    print(' '.join(list_of_letters))
    print()

    while number_of_guesses != 0:
        Validate_Guess(Guess_Choice())
            

Validate_Guess(Guess_Choice())