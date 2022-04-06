import random

play_game = True

# Initialize set of previous_words 
# Previous_words prevents duplicate words from appearing in game
previous_words = set()

# Initialize Score Board Totals
Wins = 0
Losses = 0

# While loop keeps game going if player opts to continue playing game
while play_game == True:

    # Print current score
    print(f"Wins: {Wins}\nLosses: {Losses}")
    print()

    # Read words from dictionary file
    f = open('words_alpha.txt')
    dict_lines = f.read().splitlines()
    f.close()

    # Initialize dictionary_set
    dictionary_set = set()

    # Add words from file to dictionary_set
    for line in dict_lines:
        dictionary_set.add(line)

    # Remove words from previous games
    dictionary_set = dictionary_set - previous_words

    # Choose a random word from the dictionary
    correct_word = random.choice(tuple(dictionary_set))

    # Add correct_word to set of previous_words
    previous_words.add(correct_word)

    # Initialize player_guesses and list of letters displayed to screen
    number_of_guesses = 7
    list_of_letters = []

    # For each letter add an underscore to list_of_letters
    for letter in correct_word:
        if letter.isalpha():
            list_of_letters.append("_")
        else:
            list_of_letters.append(letter)

    # Print list of underscores to screen
    print(' '.join(list_of_letters), end = "\n\n" )


    # Function Guess_Choice() prompts user to guess a letter or a word
    # User can enter "letter" or "l" to guess a letter and "word" or "w" to guess a word

    def Guess_Choice():

        # Ask user to guess a word or a letter
        guess_choice = input('Do you want to guess a letter (L) or a word (W)?: ').lower()
        print()
        valid_choice = False

        # If guess is a word, guess_choice = 0
        # If guess is a letter, guess_choice = 1
        # If input is invalid, prompt user for a proper response
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
        

    # Function Validate_Guess takes input choice and prompts user for either
    # a word (if choice = 0) or a letter (if choice = 1) and ensures they are valid
    # Returns the guess (letter or word) and choice (0 or 1)

    def Validate_Guess(choice):

        # Ask user to guess a valid word (if invalid prompt them again)
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
        
        # Ask user to guess a valid letter (if invalid prompt them again)
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

    # Function Update_Board takes inputs of guess (letter or word) and choice (0 or 1)
    # Updates board on console
    # Updates number of guesses
    # Updates Score board

    def Update_Board(guess, choice):
        
        # Global variable list
        global number_of_guesses
        global list_of_letters
        global correct_word
        global Wins
        global Losses

        # If user guesses a word:
        if choice == 0:

            # If guess is correct, print congralutory message and show the word, increment wins by 1
            if guess == correct_word:
                list_of_letters = list(correct_word)
                print("You win!\n")
                print("The word was \n")
                number_of_guesses = 0
                Wins+=1
            
            # If guess is incorrect, print remaining guesses, increment losses if necessary
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

        # If guess is a letter
        else:

            # If guess is correct, update board with letters
            if any(letter in correct_word for letter in guess):
                print("Correct!\n")
                for i in range(0,len(correct_word)):
                    if guess == list(correct_word)[i]:
                        list_of_letters[i] = guess
            
            # If guess is incorrect, decrement number of guesses, print remaining guesses, and increment losses if necessary
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

        # Show current state of the board
        print(' '.join(list_of_letters))
        print()

        # While player has guesses remaining, repeat guessing process
        while number_of_guesses != 0:
            Guess, Choice = Validate_Guess(Guess_Choice())
            Update_Board(Guess, Choice)

    # Starts initial guessing process
    Guess, Choice = Validate_Guess(Guess_Choice())
    Update_Board(Guess, Choice)

    # If game is over, ask player to play again
    if number_of_guesses == 0:
        play_again = input("Do you want to play again? (y/n): ").lower()
        print()

        # Reject invalid inputs (valid inputs are 'y' or 'yes' and 'n' or 'no')
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