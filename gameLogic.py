import random as r
board=[    [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           ]
UI = {0:"~", 11:"#", 10:"X",  1:"~", 2:"~", 3:"~", 4:"~", 5:"~", 6:"~", 7:"~", 8:"~", 9:"~"}

#_______________________________________________________________
def cheats():
    global UI
    UI = {0:"~", 11:"#", 10:"X", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
#_______________________________________________________________
def rand(lowerB, upperB):
    return r.randint(lowerB, upperB)  

#_______________________________________________________________
def board_Clear(board, item):
    for cout1, i in enumerate(board):
            for cout2, j in enumerate(i):
                if j == item:
                    board[cout1][cout2] = 0

#_______________________________________________________________
def gen_Ship(size):
    alert = False
    y = rand(0,9); x = rand(0,9)
    choose1 = rand(0,1); choose2 = rand(0,1)
################################################################
    if board[y][x] == 0:
        board[y][x] = size
    else:
        board_Clear(board, size)
        gen_Ship(size)
        return

    for i in range(1, size):
################################################################
        if choose1 == 1: # up/down
################################################################
            if choose2  == 1:
                if y+size > 9 or board[y+i][x] != 0:
                    alert = True
                    break
                board[y+i][x] = size 
################################################################
            else:
                if y-size < 0 or board[y-i][x] != 0:
                    alert = True
                    break
                board[y-i][x] = size #
################################################################
        else: # left/right
################################################################
            if choose2 == 1:
                if x+size > 9 or board[y][x+i] != 0:
                    alert = True
                    break
                board[y][x+i] = size 
################################################################
            else:
                if x-size < 0 or board[y][x-i] != 0:
                    alert = True
                    break
                board[y][x-i] = size 

    if alert == True:   
        board_Clear(board, size)
        gen_Ship(size)         

#_______________________________________________________________
def printboard():
    print("   1 2 3 4 5 6 7 8 9 10")
    for num, i in enumerate(board):
        line = str(num+1)+" "
        if num+1 == 10:
            line = str(num+1)
        for j in i:
            line +=" "+UI[j]
        print(line)
    print("\n")

#_______________________________________________________________
def shoot():
################################################################
    while True:
        x = int(input("Choose your X coordinate: ")) - 1
        y = int(input("Choose your Y coordinate: ")) - 1
        print("\n")
        prevItem = board[y][x]
        if board[y][x] == 0:
            board[y][x] = 11
            break
        elif board[y][x] > 0 and board[y][x] < 10:
            board[y][x] = 10
            break
        else:
            print("You've already shot there, choose again!")
################################################################
    found = False
    for i in board:
                for j in i:
                    if j == prevItem:
                        found = True
################################################################
    printboard()
    if found == False:
        print("A {} ship has been destroyed\n".format(str(prevItem)))
        return 1
    else:
        return 0