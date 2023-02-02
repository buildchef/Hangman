import random
#-- https://docs.python.org/3/library/random.html

import os
#-- https://docs.python.org/3/library/os.html
 
os.system('cls')


with open('random_words.txt', 'r') as file:
    """Opening the file that store our words."""
    list_ = file.read().split()
    rand_word = random.choice(list_)

def blink_word():
    """Function that create a string of '*' with the same size of the sorted word"""
    foo = []
    for letter in rand_word:
        foo.append('*')
    blink = ''.join(foo)
    return blink

def validate(letter, word, blin):
    """Function to validate if a certain letter exists in the drawn word """
    #-- if the chosen letter is in word...
    if letter in word:
        sum = 0
        list_index = []

        #-- Finding the index of the letter in the word and storing them in a list
        for _ in word:
            sum += 1
            if _ == letter:
                list_index.append(sum)

        #-- Resetting the sum variable and create a new list to reform the blink word
        sum = 0
        new_list = []

        #-- Using the indexes we extracted, we define where we will position the chosen letter
        for _ in blin:
            sum +=1
            if sum in list_index:
                new_list.append(letter)
            else:
                new_list.append('*')

        #-- Finally, we transform the modified list in a string and return that.
        blin = ''.join(new_list)
        return blin


if __name__ == '__main__':
    #-- testing the new function
    print(validate('b', 'banana', '******'))