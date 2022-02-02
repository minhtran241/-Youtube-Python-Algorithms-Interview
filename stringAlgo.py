'''
1. Reverse string:
Given a string of words, reverse all the words

start = 'This is the best'
finish = 'best the is This'

'''

from calendar import c


def split(str):
    i = 0
    length = len(str)
    spaces = [' ']
    words = []
    while i < length:
        if str[i] not in spaces:
            word_start = i
            while i < length and str[i] not in spaces:
                i += 1
            words.append(str[word_start:i])
        i += 1
    return words

def reverse_string(str):
    return ' '.join(split(str)[::-1])

print(reverse_string('This is the best'))

'''
2.1. Unique characters in Strings:
Given a string, are all characters unique?
should give a True or False to return 

Uses python built in structures

'''

def is_unique1(str):
    str = str.replace(' ', '')
    return len(set(str)) == len(str)

'''
2.2. Unique characters in Strings:
Given a string, are all characters unique?
should give a True or False to return 

'''

def is_unique2(str):
    str = str.replace(' ', '')
    characters = set()

    for letter in str:
        if letter in characters:
            return False
        else:
            characters.add(letter)
    return True

'''
3. Non repeat element:
Take a string and return character that never repeats
if multiple uniques then return only the first unique

'''

def non_repeating(str):
    str = str.replace(' ', '').lower()
    
    char_count = {}

    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # for char, count in char_count.items():
    #     if count == 1:
    #         return char
    # return None
    all_uniques = [char for char, count in char_count.items() if count == 1]
    return all_uniques