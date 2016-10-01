# -*- coding: utf-8 -*-
"""
decrease increment size----->slower program
increasing epsilon--------->less accurate answer

@author: ibrahim
"""

cube = float(input("Please enter a number: "))
epsilon = 0.01
guess = 0.0
increment = 0.01
num_guesses = 0.0

while(abs(guess**3 - float(cube)) >= epsilon) and (guess <= cube):
    guess += increment
    num_guesses += 1
    
print('num_guesses =', num_guesses)

if((abs(guess**3) - cube) >= epsilon):
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)