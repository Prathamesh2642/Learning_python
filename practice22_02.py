def game():
    return (input("Enter new score "))
hisc=open('Hiscore.txt','r')
check=hisc.read() #.read() can work only once after opening
if(len(check)==0):
    userHscore=game()
    with open("Hiscore.txt",'w') as newuserHscore:
        newuserHscore.write(userHscore)
        print("This part is executed")
else:
    user_H_score=game()
    print(check)
    print(user_H_score)
    if check>user_H_score:
        pass
    else:
        with open('Hiscore.txt','w') as newh:
            newh.write(str(user_H_score))
            print("This is exec")

