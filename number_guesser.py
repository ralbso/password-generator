"""
Created on Sun Jun 11 23:28:25 2017

@author: Raul
"""

print('Please think of a number between 0 and 100!')

high = 100
low = 0
correct = False

while not correct:
    guess = (high+low)//2
    print('Is your secret number ' + str(guess) + '?')
    print("Enter 'h' to indicate the guess is too high.", end = ' ')
    print("Enter 'l' to indicate the guess is too low.", end = ' ')
    print("Enter 'c' to indicate I guessed correctly.", end = ' ')
    usrin = str(input())
    
    if usrin == 'c':
        correct = True
    elif usrin == 'h':
        high = guess
    elif usrin == 'l':
        low = guess
    else:
        print('Sorry, I did not understand your input.')
        
print('Game over. Your secret number was:', + guess)
