import random

b=random.randint(1,100)
count=0
while True:
  a=int(input("Enter a number "))
  count+=1
  if a==b:
    print(f"You guessed the right number in {count} tries")
    break
  elif a>b:
    print("You guessed a higher number")
  else:
    print("You guessed a lower number")

