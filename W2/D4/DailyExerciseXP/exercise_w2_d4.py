import random

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

file_name = 'starwars_names.txt'

file_path = os.path.join(dir_path, file_name)

def get_words_from_file(file_path):
    '''get_words_from_file(file_path)
       Return the list of words.'''
    with open(file_path, "r", encoding='utf-8') as f:
        return f.read().split()
    
def get_random_sentence (sentence_length):
    '''get_random_sentence (sentence_length)
       Return the sentence.'''
    list_of_words = get_words_from_file(file_path)
    new_sentence = ''
    for i in range(sentence_length):
        new_sentence += ' ' + random.choice(list_of_words)
    return new_sentence.lower().strip()

def main():
    print('=' * 50)
    print("This program generates a random sentence using words from a predefined file.")
    print("In this example, the file contains Star Wars character names.")
    print("You will be asked to enter how many words you want in the sentence (between 2 and 20).")
    print()

    user_input = input('Enter the number of words in the sentence you want to generate (2–20): ')
    try:
        user_input = int(user_input)
        if user_input < 2 or user_input >20:
            print('Number is out of range (2-20)')
            return
    except ValueError:
        print('Not valid number')
        return
        
    print(f"Here is your sentence: \n{get_random_sentence(user_input)}")


main()
print('=' * 50)



