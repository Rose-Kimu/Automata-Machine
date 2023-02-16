import unittest
from unittest.mock import patch

def language_l1():
    print('This is L1: checks whether the input string ends with certain letter/digit')


    alphabet_one = input('Enter the first letter of the alphabet: ')
    alphabet_two = input('Enter the second letter of the alphabet: ')

    alphabet = [alphabet_one, alphabet_two]
    ends_with = alphabet_one
    print(f' This language tests for strings ending with {alphabet_one}')

    initial_state = 'A'
    final_state = 'B'

    transitions = {  'A':{alphabet_one:'B', alphabet_two:'A'},
                    'B':{alphabet_one:'B', alphabet_two:'A'}
    }

    string = input('Enter the string to be tested here: ')
    while string != 'q':
        present_state = initial_state
        for i in string:
            try:
                present_state = transitions[present_state][i]
                execute = True
            except:
                execute = False
                # print('Enter a  string with letters of specified alphabet')
                break
        
        if present_state == final_state and execute == True:
            print('String accepted')
            accepted = 'True'

        elif present_state != final_state and execute == True:
            print('String rejected')
            accepted = 'False'

        else:
            print('STRING LETTERS ABSENT FROM THE ALPHABET')
            accepted = 'Invalid'
            
        string = input('Enter the string to be tested here: ')
    return accepted
        # string = string_function()



def language_l2():
    print('This is L2: checks whether the input string starts and ends with certain letter/digit')
    print('Enter the Alphabet')

    alphabet_one = input('Enter the first letter of the alphabet: ')
    alphabet_two = input('Enter the second letter of the alphabet: ')

    alphabet = [alphabet_one, alphabet_two]
    ends_with = alphabet_one
    print(f' This language tests for strings starting with {alphabet_one} ending with {alphabet_two}')

    initial_state = 'A'
    final_state = 'D'

    transitions = {  'A':{alphabet_one:'B', alphabet_two:'E'},
                    'B':{alphabet_one:'B', alphabet_two:'D'},
                    'D':{alphabet_one:'B', alphabet_two:'D'},
                    'E':{alphabet_one:'E', alphabet_two:'E'}
    }

    string = input('Enter the string to be tested here: ')
    while string != 'q':
        present_state = initial_state
        for i in string:
            try:
                present_state = transitions[present_state][i]
                execute = True
            except:
                execute = False
                # print('Enter a  string with letters of specified alphabet')
                break
        
        if present_state == final_state and execute == True:
            print('String accepted')
            accepted = 'True'

        elif present_state != final_state and execute == True:
            print('String rejected')
            accepted = 'False'

        else:
            print('STRING LETTERS ABSENT FROM THE ALPHABET')
            accepted = 'Invalid'

        string = input('Enter the string to be tested here: ')
        # string = string_function()
    return accepted

def choose_language():
    language = int(input('Enter the language to test for. 1 for L1 or 2 for L2: '))
    if language == 1:
        language_l1()
    elif language == 2:
        language_l2()

if __name__ == "__main__":
    choose_language()

# This is my main file