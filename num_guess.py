import random

print("Select Range:")

i=int(input("Enter your first integer="))
f=int(input("Enter your last integer="))

if (f-i)>0:
    print("Go ahead!")

else:
    print("Invalid range!Try again!!")
attempts=0
com=random.randint(i,f)
while True:


    n=int(input("Guess a number:"))
    attempts+=1

    if com==n:
        print("Congratulations!You are correct")
        
        print("Total Attempts:",attempts)
        break


    elif (com-n)>0:
        print("It's Small! Try a larger one!")


    else:
        print("It's Large! Try a Smaller one!")


