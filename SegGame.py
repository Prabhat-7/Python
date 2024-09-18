import random as r
outcomes=[[0,1,-1],[-1,0,1],[1,-1,0]]
start=True
mode=input("Play with friend or computer?(f/c):")
while start:
    match mode:
        case "c":

            try:
                choice=int(input("Enter '0' for Snake , '1' for Water and '2' for Gun:"))
                outcome=outcomes[choice][r.choice(range(3))]

                if outcome==1:
                    print("Congratulations!! you won.")

                elif outcome==0:
                    print("It was a draw.")

                else:
                    print("You lost unfortunately.")
            except:
                print("Invalid Input")
            
        case "f":
            
                try:
                    p1=int(input("Player 1,enter '0' for Snake , '1' for Water and '2' for Gun:"))
                    p2=int(input("Player 2,enter '0' for Snake , '1' for Water and '2' for Gun:"))
                    outcome=outcomes[p1][p2]
                    if outcome==1:
                        print("Congratulations!! Player 1 won.")
            
                    elif outcome==0:
                        print("It was a draw.")

                    else:
                        print("Congratulations!! Player 2 won.")
                except:
                    print("Invalid Input")
                
        case _:
            print("Invalid input")
    start=bool(int(input("Wanna play again?(0/1)")))
            
        