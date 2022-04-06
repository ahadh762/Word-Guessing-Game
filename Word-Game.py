correct_word = "champion"
number_of_guesses = 7

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

# def Validate_Guess(guess_choice):
#     if guess_choice = 0:

