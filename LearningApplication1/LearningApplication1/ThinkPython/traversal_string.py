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

print(sys.stdin.encoding) 
os.chdir('\\\\anglicare-sa.org.au\\files\\frank.wang\\My Documents\\Learning\\Python\\LearningApplication1\\LearningApplication1\\ThinkPython')
fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)
