import os
from platform import system
import random
from turtle import pos
from five_letter_words import five_letters_extensive, five_letters_ranked, common_letters_ranked, starting_words
os.system('cls')



def solve_wordle():
    possible_words = five_letters_ranked
    possible_words_ext = five_letters_extensive
    letters = common_letters_ranked
    poss_letters = []
    wrong_letters = []
    word_key = [0, 0, 0, 0, 0] #what is know at current state? i.e., [0, 0, 1, 0, -1]         0 = wrong, 1 = correct, -1 = misplaced
    turn = 0
    w = 0 #this variable affects the index of possible_words[]


    #start loop
    while word_key != [1, 1, 1, 1, 1]:
        os.system('cls')
        
        #comp gives user a word
        if turn == 0:
            guess = random.choice(starting_words)
        elif len(possible_words) > 0:
            guess = possible_words[w]
        elif len(possible_words) == 0 and len(possible_words_ext) > 0:
            guess = random.choice(possible_words_ext)
        else:
            os.system('cls')
            print('Could not find a valid word to guess')
            input()
            break
            
        guess_letters = list(guess)

        print(f'Try the word  > "{guess}" <\n')
        next = input('---\nPress \'enter\' to continue\nOr type \'n\' for a new word: ').lower()
        
        #press 'n' for new word to guess
        if next == 'n':
            w += 1
            continue
        
        w = 0 #reset index if user asked for a dif word

        #user inputs results
        #x = wrong
        #c = correct
        #m = missplaced
        for i in range(5):            
            sel_string = "     "
            os.system('cls')
            print(' '.join(guess_letters))
            print(' '.join(sel_string[:i] + '^' + sel_string[i+1:]) + '\n')

            if word_key[i] == 1:
                input(f'Skipping correct letter "{guess_letters[i]}". ')
                continue

            letter_key = input(f'---\nif wrong type "x"\nif correct type "c"\nif misplaced type "m"\n---\n\nFeedback for letter "{guess_letters[i]}"? ').lower()

            if letter_key == 'x':
                word_key[i] = 0
            elif letter_key == 'c':
                word_key[i] = 1
            elif letter_key == 'm':
                word_key[i] = -1
            else:
                print('Invalid input. Letter was assumed to be \'wrong\'...')
                word_key[i] = 0
                input('(press \'Enter\' to continue)')


        
        if word_key == [1, 1, 1, 1, 1]:
            break

        #comp eliminates wrong letters and protects possible/correct letters
        for i in range(5):
            if word_key[i] == 0 and guess_letters[i] not in wrong_letters and guess_letters[i] not in poss_letters:
                letters.remove(guess_letters[i])
                wrong_letters.append(guess_letters[i])
            elif word_key[i] != 0 and guess_letters[i] not in poss_letters:
                poss_letters.append(guess_letters[i])
            elif word_key[i] == 0 and guess_letters[i] in poss_letters:
                #remove words that have this double letter
                possible_words = [word for word in possible_words if word.count(guess_letters[i]) < 2]

        #comp eliminates all words that contain wrong letters
        possible_words = [word for word in possible_words if all(x not in word for x in wrong_letters)]
        possible_words_ext = [word for word in possible_words_ext if all(x not in word for x in wrong_letters)]
        
        #comp narrows list to words with that contain misplaced letters somewhere
        for i in range(5):
            if word_key[i] == -1:
                possible_words = [word for word in possible_words if guess_letters[i] in word]
                possible_words_ext = [word for word in possible_words_ext if guess_letters[i] in word]

        #comp elimates words with letters that in theory be misplaced but are correct
        for i in range(5):
            if word_key[i] == -1:
                possible_words = [word for word in possible_words if word[i] != guess_letters[i]]
                possible_words_ext = [word for word in possible_words_ext if word[i] != guess_letters[i]]

        #comp narrows list to words with letters in correct places
        for i in range(5):
            if word_key[i] == 1:
                possible_words = [word for word in possible_words if word[i] == guess_letters[i]]
                possible_words_ext = [word for word in possible_words_ext if word[i] == guess_letters[i]]

  

        print(f'Possible words: {len(possible_words)}')
        input('(press \'Enter\' to continue)')
        turn += 1
        if turn > 5:
            os.system('cls')
            print("I'm sorry, you ran out of turns to win :(")
            input()
            break
    #end loop

    if word_key == [1, 1, 1, 1, 1]:
        os.system('cls')
        print('***Congratulations! You won today\'s Wordle!***')
        input()


solve_wordle()