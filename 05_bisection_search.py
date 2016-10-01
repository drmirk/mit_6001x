# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 14:28:22 2016

@author: mdibr
"""

start = 0
end = 100
print("Please think of a number between 0 and 100!")
while(True):
    middle = int((start + end)/2)
    print("Is your secret number " + str(middle) +"?")
    inpu = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if(inpu == "h"):
        end = middle
    elif(inpu == "l"):
        start = middle
    elif(inpu == "c"):
        print("Game over. Your secret numbehr was:", middle)
        break
    else:
        print("Sorry, I did not understand your input.")
        