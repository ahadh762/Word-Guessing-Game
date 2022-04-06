import random

play_game = True
previous_words = set()
Wins = 0
Losses = 0

while play_game == True:
    print(f"Wins: {Wins}\nLosses: {Losses}")
    print()
    f = open('words_alpha.txt')
    dict_lines = f.read().splitlines()
    f.close()

    dictionary_set = set()

    for line in dict_lines:
        dictionary_set.add(line)

    dictionary_set = dictionary_set - previous_words

    correct_word = random.choice(tuple(dictionary_set))
    previous_words.add(correct_word)

    number_of_guesses = 7
    list_of_letters = []

    for letter in correct_word:
        if letter.isalpha():
            list_of_letters.append("_")
        else:
            list_of_letters.append(letter)

    print(' '.join(list_of_letters), end = "\n\n" )


    def Guess_Choice():

        guess_choice = input('Do you want to guess a letter (L) or a word (W)?: ').lower()
        print()
        valid_choice = False

        while (valid_choice == False):
            if guess_choice == "word" or guess_choice == "w":
                valid_choice = True
                guess_choice = 0
            elif guess_choice.lower() == "letter" or guess_choice == "l":
                valid_choice = True
                guess_choice = 1
            else:
                print(f'Invalid input: "{guess_choice}".', end = ' ')
                guess_choice = input('Do you want to guess a letter (L) or a word (W)?: ').lower()
                print()
        return guess_choice
        

    def Validate_Guess(choice):

        if choice == 0:
            guess = input("Guess a word: ").lower()
            print()
            valid_word = guess in dictionary_set
            while valid_word == False:
                print(f'Invalid word: "{guess}".', end = ' ')
                guess = input('Guess a word: ').lower()
                print()
                valid_word = guess in dictionary_set
            return guess, choice
        else:
            guess = input("Guess a letter: ").lower()
            print()
            valid_letter = guess.isalpha()
            while (valid_letter == False or len(guess) != 1) :
                print(f'Invalid letter: "{guess}".', end = ' ')
                guess = input('Guess a letter: ').lower()
                print()
                valid_letter = guess.isalpha()
            return guess, choice


    def Update_Board(guess, choice):

        global number_of_guesses
        global list_of_letters
        global correct_word
        global Wins
        global Losses

        if choice == 0:
            if guess == correct_word:
                list_of_letters = list(correct_word)
                print("You win!\n")
                print("The word was \n")
                number_of_guesses = 0
                Wins+=1
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
                    Losses+=1
        else:
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
                    Losses+=1

        print(' '.join(list_of_letters))
        print()

        while number_of_guesses != 0:
            Guess, Choice = Validate_Guess(Guess_Choice())
            Update_Board(Guess, Choice)

    Guess, Choice = Validate_Guess(Guess_Choice())
    Update_Board(Guess, Choice)

    if number_of_guesses == 0:
        play_again = input("Do you want to play again? (y/n): ").lower()
        print()
        while (play_again != 'n' and play_again != 'y') and (play_again != 'no' and play_again != 'yes') :
            print(f'Invalid input: "{play_again}".', end = ' ')
            play_again = input("Do you want to play again? (y/n): ").lower()
            print()
        if play_again == 'y':
            continue
        else:
            play_game = False
            print("Thank you for playing!\n")
            print(f"Wins: {Wins}\nLosses: {Losses}")
            print()