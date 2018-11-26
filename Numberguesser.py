#Sidhant Puntambekar
#Number Guesser

import random

#Computer to pick number
correctAnswer = random.randint(1,10)

#user guess
guess = input("Please enter a guess between 1 and 10: ")
guess=int(guess)

#see if they were right or wrong
if guess == correctAnswer:
    print ("Yay! You guessed correctly")

elif(guess>correctAnswer):
    print ("You LOSE")
    print ("You're guess was too high!")
    print ("The correct answer was", correctAnswer)
    
else:
    print ("You LOSE")
    print ("You're guess was too low!")
    print ("The correct answer was", correctAnswer)
    
 
