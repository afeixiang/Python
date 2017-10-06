'''
A function that traversal strings
'''
import os
import sys

def traversal(fruit):
    '''
    This function prints all letters in string fruit

    fruit:string
    '''
    index = 0
    while index < len(fruit):
        letter = fruit[len(fruit)-1-index]
        print(letter)
        index = index + 1

def for_traversal(fruit):
    '''
    This function prints all letters in string fruit

    fruit:string
    '''
    for letter in fruit:
        print(letter)

def ack_function():
    '''
    This function generates a serier of names.
    '''
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'

    for letter in prefixes:
        print(letter + suffix)

def count20(word):
    '''
    Count the word whether length is 20 or not, whitespace not counted

    word:string
    '''
    word.replace(' ', '')
    if len(word) == 20:
        return True
    return False

def has_no_e(word):
    '''
    Return true if there is a letter e in the word, otherwise false

    word:string
    '''
    return 'e' in word

def read_file():
    '''
    Read the word file for exercise functions.
    '''
    os.chdir('\\\\anglicare-sa.org.au\\files\\frank.wang\\My Documents\\Learning\\Python\\LearningApplication1\\LearningApplication1\\ThinkPython')
    return open('words.txt')

def exercise9_1():
    '''
    Read the words in word.txt and print the words whose length are 20.
    '''    
    fin = read_file()
    for line in fin:
        word = line.strip()
        if count20(word):
            print(word)
    print('Done!')

def exercise9_2():
    '''
    Read the words in word.txt and print the words have no letter e and calculate the rate
    '''
    fin = read_file()
    all_word = 0
    count_word = 0
    for line in fin:
        word = line.strip()
        if not(has_no_e(word)):
            print(word)
            count_word = count_word + 1
        all_word = all_word + 1
    print('Total words: ', all_word)
    print('No e words: ', count_word)

def nested_sum(t):
    '''
    Calculate the sum of the nested integer lists in list t    
    print(nested_sum([[1, 2], [3], [4, 5, 6]]))

    t:nested integer list
    '''
    total = 0
    for s in t:
        total += sum(s)
    return total
