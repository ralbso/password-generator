"""
Created on Wed Apr  5 11:19:56 2017

@author: Raul
"""
import random
import string
import time


usrinput = input('PASSWORD GENERATOR \nWould you like to create a password? (y/n) \n> ')

def createPw(usrin):
    if usrin.lower() == 'y':
        pwstrength = input('Would you like a strong or weak password? (s/w) \n> ')
        if pwstrength == 's':
            alphabet = string.ascii_letters + string.digits + '!@#$%^&*'
            strongPassword = (random.sample(alphabet,10))
            return(''.join(strongPassword))
        elif pwstrength == 'w':
            wordList = ['dog', 'baby', 'Joseph', 'Triss', 'imbibe', 'Tribianni', 
                        '1234567890', '1234', 'password']
            weakPassword = (random.sample(wordList,2))
            return(''.join(weakPassword))
        else:
            return(str(pwstrength) + ' is not a valid choice. Please try again.')
    elif usrin.lower() == 'n':
        return('No password requested.')
    else:
        return(str(usrin) + ' is not a valid choice. Please try again.')


start = time.time()             # Start timer
print(createPw(usrinput))
end = time.time()               # End timer

print('It took ' + str(end - start) + 's to generate this password')
