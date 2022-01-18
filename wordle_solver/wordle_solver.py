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

    #start loop
    while word_key != [1, 1, 1, 1, 1]:
        os.system('cls')
        #comp gives user a word
        #press 'n' for new word to guess
        

        if turn == 0:
            guess = random.choice(starting_words)
        elif len(possible_words) > 0:
            guess = possible_words[0]
        elif len(possible_words) == 0 and len(possible_words_ext) > 0:
            guess = random.choice(possible_words_ext)
        else:
            os.system('cls')
            print('Could not find a valid word to guess')
            break
            
        guess_letters = list(guess)

        print(f'Try the word "{guess}"...')
        input('(press \'Enter\' to continue)')

        #user inputs results "xxcxm"
        #x = wrong
        #c = correct
        #m = missplaced
        

        for i in range(5):
            if word_key[i] == 1:
                continue
            
            sel_string = "     "
            os.system('cls')
            print(' '.join(guess_letters))
            print(' '.join(sel_string[:i] + '^' + sel_string[i+1:]) + '\n')

            letter_key = input('wrong(x), correct(c), misplaced(m): ').lower()

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


        
        ##print(word_key)
        ##print(turn)
        
        if word_key == [1, 1, 1, 1, 1]:
            break

        #comp eliminates wrong letters and protects possible/correct letters
        ##print(f'Letters before: {letters}')
        for i in range(5):
            if word_key[i] == 0 and (guess_letters[i] not in wrong_letters) and (guess_letters[i] not in poss_letters):
                letters.remove(guess_letters[i])
                wrong_letters.append(guess_letters[i])
            elif word_key[i] != 0 and guess_letters[i] not in poss_letters:
                poss_letters.append(guess_letters[i])
        ##print(f'Letters now: {letters}')
        ##print(f'Wrong letters: {wrong_letters}')

        #comp eliminates all words that contain wrong letters
        ##print(f'Possible words before: {len(possible_words)}')
        possible_words = [word for word in possible_words if all(x not in word for x in wrong_letters)]
        possible_words_ext = [word for word in possible_words_ext if all(x not in word for x in wrong_letters)]
        ##print(f'Possible words now: {len(possible_words)}')
        
        #comp narrows list to words with that contain misplaced letters somewhere
        for i in range(5):
            if word_key[i] == -1:
                possible_words = [word for word in possible_words if guess_letters[i] in word]
                possible_words_ext = [word for word in possible_words_ext if guess_letters[i] in word]
        ##print(f'Possible words and now: {len(possible_words)}')

        #comp elimates words with letters that in theory be misplaced but are correct
        for i in range(5):
            if word_key[i] == -1:
                possible_words = [word for word in possible_words if word[i] != guess_letters[i]]
                possible_words_ext = [word for word in possible_words_ext if word[i] != guess_letters[i]]
        ##print(f'Possible words and now and now: {len(possible_words)}')

        #comp narrows list to words with letters in correct places
        for i in range(5):
            if word_key[i] == 1:
                possible_words = [word for word in possible_words if word[i] == guess_letters[i]]
                possible_words_ext = [word for word in possible_words_ext if word[i] == guess_letters[i]]
        ##print(f'Possible words and now and now and now: {len(possible_words)}')

        #if multiple letters in guess and word only contains 1 of them...
        #do I need this condition?

        

        print(f'Possible words: {len(possible_words)}')
        input('(press \'Enter\' to continue)')
        turn += 1
        if turn > 5:
            os.system('cls')
            print("I'm sorry, you ran out of turns to win :(")
            break
    #end loop

    if word_key == [1, 1, 1, 1, 1]:
        os.system('cls')
        print('***Congratulations! You won today\'s Wordle!***')
        input()


solve_wordle()