from PyDictionary import PyDictionary
dictionary = PyDictionary()

def Guess_Choice():
    guess_choice = input('Do you want to guess a letter or a word?: ')
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
    return guess_choice

def Validate_Guess(choice):
    if choice == 0:
        guess = input("Guess a word: ")
        valid_word = bool(dictionary.meaning(guess, True))
        while valid_word == False:
            guess = input("Invalid input. Guess a word: ")
            valid_word = bool(dictionary.meaning(guess,True))
    else:
        guess = input("Guess a letter: ")
        valid_letter = guess.isalpha()
        while valid_letter == False or len(guess) != 1:
            guess = input("Invalid input. Guess a letter: ")
            valid_letter = guess.isalpha()
    return guess.lower()

print(Validate_Guess(Guess_Choice()))