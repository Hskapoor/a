print("Welcome to the Game")

playing = input("Do you wan to play ")

if playing.lower() != "yes":
    quit()
else:   
    print("Okay lets Play !")    

score=0
answer=input("What is CPU ? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score +=1
else:   
    print('Incorrect!')

answer = input("What is GPU ? ")
if answer.lower() == "Graphics processing unit":
    print('Correct!')
    score +=1
else:   
    print('Incorrect!')

answer=input("What is RAM ? ")
if answer.lower() == "Random Access Memory":
    print('Correct!')
    score +=1
else:   
    print('Incorrect!')

answer=input("What is PU ? ")
if answer.lower() == "power unit":
    print("Correct !")
    score +=1
else:   
    print("Incorrect !")

print("You Got " + str(score) + " Questions Correct!" )
print("You Got " + str(((score/4)*100))+ "%.")