import random
def game(i,com):
    if(i=='s'):
        if(com=='p'):
            print("Computer won")

        elif(com=='c'):
            print("You won")
        elif(com=='s'):
            print("Tie")
    elif(i=='p'):
        if(com=='s'):
            print("You won")
        elif(com=='c'):
            print("computer won")
        elif(com=='p'):
            print("Tie")
    elif(i=='c'):
        if(com=='p'):
            print("You won")
        elif(com=='s'):
            print("computer won")
        elif(com=='c'):
            print("Tie")


turns=int(input("Enter number of turns "))


j=0
while j<turns:
    print("Your turn:Choose Stone(s),paper(p),scissor(c): ")
    i=input()
    print("Computer turn:Choose Stone(s),paper(p),scissor(c):  ")
    ran=random.randint(1,3)
    if(ran==1):
        com='s'
    elif(ran==2):
        com='p'
    elif(ran==3):
        com='c'
        
    if(i=='s'):
        if ran==1:
            print("You chose stone and computer chose stone")
        elif ran==2:
            print("You chose stone and computer chose paper")
        elif ran==3:
            print("You chose stone and computer chose scissors")
    elif(i=='p'):
        if ran==1:
            print("You chose paper and computer chose stone")
        elif ran==2:
            print("You chose paper and computer chose paper")
        elif ran==3:
            print("You chose paper and computer chose scissors")
    elif(i=='c'):
        if ran==1:
            print("You chose scissors and computer chose stone")
        elif ran==2:
            print("You chose scissors and computer chose paper")
        elif ran==3:
            print("You chose scissors and computer chose scissors")
    game(i,com)
    j+=1