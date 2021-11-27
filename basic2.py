import random

top_of_range = input("Enter the number max for random")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
if top_of_range<=0:
    print("Please enter no More than 0 next time !")
    quit()
    
random_no= random.randint(0,top_of_range)

guess=0

while True:
    guess += 1
    user_guess=input("Input Guess No:")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number next time:")
        continue
    
    
    if user_guess == random_no:
        print("Hey You Got it !") 
        break
    
    elif user_guess<random_no:
        print("Hey Guess is less than Random No")
    
    else: 
        print("You are Above the number")
print("You have made", guess,"Guesses")