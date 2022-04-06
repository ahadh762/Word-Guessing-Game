from PyDictionary import PyDictionary
dictionary = PyDictionary()

correct_word = "champion".lower()
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
    return guess_choice

def Validate_Guess(choice):
    if choice == 0:
        guess = input("Guess a word: ")
        valid_word = bool(dictionary.meaning(guess, True))
        while valid_word == False:
            guess = input("Invalid input. Guess a word: ").lower()
            valid_word = bool(dictionary.meaning(guess,True))
        if guess == correct_word:
            print("You win!")
        else:
            print("Incorrect! You lose a guess!")
    else:
        guess = input("Guess a letter: ")
        print()
        valid_letter = guess.isalpha()
        while valid_letter == False or len(guess) != 1:
            guess = input("Invalid input. Guess a letter: \n\n").lower()
            valid_letter = guess.isalpha()
        if any(letter in correct_word for letter in guess):
            print("Correct!")
            for i in range(0,len(correct_word)):
                if guess == list(correct_word)[i]:
                    list_of_letters[i] = guess
        else:
            print("Incorrect! You lose a guess!\n\n")

        print(' '.join(list_of_letters))
            

Validate_Guess(Guess_Choice())