import random

print("""WELCOME TO THE TREASURE HUNT GAME!!
      Your mission is to find the hidden treasure!!!""")

rows=int(input("Enter Your Row Range:"))
cols=int(input("Enter Your column Range:"))


treasure_row=random.randint(0,rows-1)
treasure_col=random.randint(0,cols-1)
grid = [["⬜" for _ in range(cols)] for _ in range(rows)]
def show_grid():
    print("Your guess map:")

    for r in grid:
        print(" ".join(r))
show_grid()
attempts=0
while True:


    user_choice_row=int(input("Guess the row (1 to {}): ".format(rows))) - 1
    user_choice_col=int(input("Guess the column (1 to {}): ".format(cols))) - 1
    attempts+=1
    if (treasure_row==user_choice_row) and (treasure_col==user_choice_col):

        grid[user_choice_row][user_choice_col]="🪙"
        show_grid()
        print("Congatulations!! You won")
        print("Total Attempts:" ,attempts)
        break

    grid[user_choice_row][user_choice_col]="❌"
    show_grid()

    if abs(treasure_row-user_choice_row)<=1 and abs(treasure_col-user_choice_col)<=1:

        print("You are very colse!")
        

  
    else:
        print("You are far away!")

    choice = input("Do you want a hint? (a)Yes / (b)No: ").lower()
    
    if choice.lower()=='a':


        if user_choice_row < treasure_row:
             
           row_hint="Go Down"

        elif user_choice_row > treasure_row:
           row_hint="Go Up"

        else:
           row_hint=""

        if user_choice_col < treasure_col:
           col_hint="Go Right"

        elif user_choice_col > treasure_col:
           col_hint="Go Left"

        else:
           col_hint=""
        
        print("Hint:",row_hint+("-" if row_hint and col_hint else "") + col_hint )
        
    elif choice.lower()=='b':
        pass

    else:
        print("Invalid Choice!")

    



        

    