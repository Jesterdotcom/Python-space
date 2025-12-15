from display import design
design()

ans = "y"

p1 = input("Enter Player 1 name = ")
p2 = input("Enter Player 2 name = ")

def check():
        global r
        r = 0
        if (
            l[0] == l[1] == l[2] == "X"
            or l[3] == l[4] == l[5] == "X"
            or l[6] == l[7] == l[8] == "X"
        ):  # for X rows
            print(p1, "win")
            r = 1
        elif (
            l[0] == l[1] == l[2] == "O"
            or l[3] == l[4] == l[5] == "O"
            or l[6] == l[7] == l[8] == "O"
        ):  # for O rows
            print(p2, "win")
            r = 1
        elif (
            l[2] == l[4] == l[6] == "X" or l[0] == l[4] == l[8] == "X"
        ):  # for X diagonals
            print(p1, "win")
            r = 1
        elif (
            l[2] == l[4] == l[6] == "O" or l[0] == l[4] == l[8] == "O"
        ):  # for O diagonals
            print(p2, "win")
            r = 1
        elif (
            l[0] == l[3] == l[6] == "X"
            or l[1] == l[4] == l[7] == "X"
            or l[2] == l[5] == l[8] == "X"
        ):  # for X columns
            print(p1, "win")
            r = 1
        elif (
            l[0] == l[3] == l[6] == "O"
            or l[1] == l[4] == l[7] == "O"
            or l[2] == l[5] == l[8] == "O"
        ):  # for O columns
            print(p2, "win")
            r = 1

def board():
    global h,g
    h = "|"
    g = "---------"
    print(l[0], h, l[1], h, l[2])
    print(g)
    print(l[3], h, l[4], h, l[5])
    print(g)
    print(l[6], h, l[7], h, l[8]) 

while ans == "y":
    lft = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # for not overputting
    l = [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ]
     
    # main printing pattern
    board()
    i,n,s,t = 0," ",["X", "O"],[p1, p2]
    print("Player", p1, " will use X and Player", p2, " will use O ")
    while n in l:
        check()
        if r == 1:
            break
        else:
            # alternating values evenodd method
            if i % 2 == 0:
                c1 = t[0]
                c2 = s[0]
            else:
                c1 = t[1]
                c2 = s[1]

            print("Player", c1, "turn")

            # user input for position
            try:
                pos = int(input("Enter on which position you want to put your symbol : "))
            except ValueError:
                print("\nError: Invalid input")
            # check inputy is in range or not
            if pos in lft:
                l[pos - 1] = c2
                lft.remove(pos)
                i += 1
            else:
                if pos >= 9:
                    print("Please enter number from 1 to 9")
                elif 1 <= pos <= 9:
                    print("OCCUPIED")
                else:
                    print("INVALID INPUT TRY AGAIN !")

            # printed the new output
            board()
            
    if n not in l:
        check()
        if r == 0:
            print("Match Draw")
        print("Want to play again ? ")
        ans = input("Type Y for Yes or N for No : ")
print("GAME CLOSED")

