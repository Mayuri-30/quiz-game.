print("welcome to my computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()
print("okay! Let's play :)") 
score = 0

answer = input("what does CPU stands for? ").lower()
if answer =="central processing unit":
    print('correct') 
    score +=1
else:
    print("Incorrect!") 

answer = input("what does GPU stands for? ").lower()
if answer =="Graphics processing unit":
    print('correct')
    score +=1 
else:
    print("Incorrect!")

answer = input("what does RAM stands for? ").lower()
if answer =="Random access memory":
    print('correct')
    score +=1 
else:
    print("Incorrect!")

answer = input("what does PSU stands for? ").lower()
if answer =="Power supply unit":
    print('correct')
    score +=1 
else:
    print("Incorrect!")
print("You got" + str(score) + "questoins correct") 

print("You got" + str((score/4)*100) + "%")                                           