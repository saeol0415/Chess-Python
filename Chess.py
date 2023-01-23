from array import *

# Creating Empty Board
board = [[0 for i in range(8)] for j in range(8)]



# Reset Function
def reset():
    for i in range(8):
        board[i] = ["a"+str(i+1),"b"+str(i+1),"c"+str(i+1),"d"+str(i+1),"e"+str(i+1),"f"+str(i+1),"g"+str(i+1),"h"+str(i+1)]

    board[0][0] = "WR"
    board[0][1] = "WN"
    board[0][2] = "WB"
    board[0][3] = "WQ"
    board[0][4] = "WK"
    board[0][5] = "WB"
    board[0][6] = "WN"
    board[0][7] = "WR"

    board[7][0] = "BR"
    board[7][1] = "BN"
    board[7][2] = "BB"
    board[7][3] = "BQ"
    board[7][4] = "BK"
    board[7][5] = "BB"
    board[7][6] = "BN"
    board[7][7] = "BR"

    for i in range(8):
        board[1][i] = "WP"

    for i in range(8):
        board[6][i] = "BP"



# Checks if a bishop move is blocked by another piece (True = Blocked, False = Not Blocked)
def isBlockedB(x1,y1,x2,y2):
    if x1 < x2:
        dirx = 1
    else:
        dirx = -1
    if y1 < y2:
        diry = 1
    else:
        diry = -1
    i = 1
    while x1+dirx*i != x2:
        if board[x1+dirx*i][y1+diry*i] != chr(y1+diry*i+97)+str(x1+dirx*i+1):
            return True
        i += 1
    return False
    


# Checks if a rook move is blocked by another piece (True = Blocked, False = Not Blocked)
def isBlockedR(x1,y1,x2,y2):
    i = 1
    if x1 == x2:
        if y1 < y2:
            diry = 1
        else:
            diry = -1
        while y1+diry*i != y2:
            if board[x1][y1+diry*i] != chr(y1+diry*i+97)+str(x1+1):
                return True
            i += 1
        return False
    elif y1 == y2:
        if x1 < x2:
            dirx = 1
        else:
            dirx = -1
        while x1+dirx*i != x2:
            if board[x1+dirx*i][y1] != chr(y1+97)+str(x1+dirx*i+1):
                return True
            i += 1
        return False



# Checks if a queen move is blocked by another piece (True = Blocked, False = Not Blocked)
def isBlockedQ(x1,y1,x2,y2):
    if (x1-x2)*(y1-y2) == 0:
        if isBlockedR(x1,y1,x2,y2) == False:
            return False
        else:
            return True
    else:
        if isBlockedB(x1,y1,x2,y2) == False:
            return False
        else:
            return True



# Checks if white's pawn move is blocked by another piece (True = Blocked, False = Not Blocked)
def isBlockedWP(x1,y1,x2,y2):
    if board[x1+1][y1][0] != chr(y1+97):
        return True
    else:
        return False



# Checks if white's pawn move is blocked by another piece (True = Blocked, False = Not Blocked)
def isBlockedBP(x1,y1,x2,y2):
    if board[x1-1][y1][0] != chr(y1+97):
        return True
    else:
        return False



# Checks if a bishop move is valid (True = Valid, False = Invalid)
def checkB(x1,y1,x2,y2):
    if abs(x1-x2) == abs(y1-y2):
        if isBlockedB(x1,y1,x2,y2) == False:
            return True
        else:
            return False
    else:
        return False



# Checks if a knight move is vaild (True = Valid, False = Invalid)
def checkN(x1,y1,x2,y2):
    if abs(x1-x2)*abs(y1-y2) == 2:
        return True
    else:
        return False



# Checks if a rook move is vaild (True = Valid, False = Invalid)
def checkR(x1,y1,x2,y2):
    if (x1-x2)*(y1-y2) == 0:
        if isBlockedR(x1,y1,x2,y2) == False:
            return True
        else:
            return False
    else:
        return False



# Checks if a queen move is vaild (True = Valid, False = Invalid)
def checkQ(x1,y1,x2,y2):
    if (x1-x2)*(y1-y2) == 0:
        if checkR(x1,y1,x2,y2) == True:
            if isBlockedQ(x1,y1,x2,y2) == False:
                return True
            else:
                return False
        else:
            return False
    else:
        if checkB(x1,y1,x2,y2) == True:
            if isBlockedQ(x1,y1,x2,y2) == False:
                return True
            else:
                return False
        else:
            return False



# Checks if a king move is vaild (True = Valid, False = Invalid) / Castling not implemented yet
def checkK(x1,y1,x2,y2):
    if (abs(x1-x2) <= 1) and (abs(y1-y2) <= 1):
        return True
    else:
        return False



# Checks if a pawn move is vaild (True = Valid, False = Invalid) / En Passant not implemented yet
def checkP(x1,y1,x2,y2):
    if board[x1][y1][0] == "W":
        if y1 == y2:
            if board[x2][y2][0] == chr(y2+97):
                if x1 == 1:
                    if x2-x1 == 2:
                        if isBlockedWP(x1,y1,x2,y2) == False:
                            return True
                    elif x2-x1 == 1:
                        return True
                else:
                    if x2-x1 == 1:
                        return True
        elif abs(y1-y2) == 1:
            if x2-x1 == 1:
                if board[x2][y2][0] == "B":
                    return True
    elif board[x1][y1][0] == "B":
        if y1 == y2:
            if board[x2][y2][0] == chr(y2+97):
                if x1 == 6:
                    if x2-x1 == -2:
                        if isBlockedBP(x1,y1,x2,y2) == False:
                            return True
                    elif x2-x1 == -1:
                        return True
                else:
                    if x2-x1 == -1:
                        return True
        elif abs(y1-y2) == 1:
            if x2-x1 == -1:
                if board[x2][y2][0] == "W":
                    return True
    return False



# Defining Move Function
def move(x1,y1,x2,y2):
    if board[x1][y1] != chr(y1+97)+str(x1+1):
        if abs(x1-x2)+abs(y1-y2) != 0:
            if board[x1][y1][0] != board[x2][y2][0]:
                if board[x1][y1][1] == "B":
                    if checkB(x1,y1,x2,y2) == True:
                        board[x2][y2] = board[x1][y1]
                        board[x1][y1] = chr(y1+97)+str(x1+1)
                    else:
                        print("Bishop at", chr(y1+97)+str(x1+1), "cannot move to", str(chr(y2+97)+str(x2+1)))
                elif board[x1][y1][1] == "N":
                    if checkN(x1,y1,x2,y2) == True:
                        board[x2][y2] = board[x1][y1]
                        board[x1][y1] = chr(y1+97)+str(x1+1)
                    else:
                        print("Knight at", chr(y1+97)+str(x1+1), "cannot move to", str(chr(y2+97)+str(x2+1)))
                elif board[x1][y1][1] == "R":
                    if checkR(x1,y1,x2,y2) == True:
                        board[x2][y2] = board[x1][y1]
                        board[x1][y1] = chr(y1+97)+str(x1+1)
                    else:
                        print("Rook at", chr(y1+97)+str(x1+1), "cannot move to", str(chr(y2+97)+str(x2+1)))
                elif board[x1][y1][1] == "Q":
                    if checkQ(x1,y1,x2,y2) == True:
                        board[x2][y2] = board[x1][y1]
                        board[x1][y1] = chr(y1+97)+str(x1+1)
                    else:
                        print("Queen at", chr(y1+97)+str(x1+1), "cannot move to", str(chr(y2+97)+str(x2+1)))
                elif board[x1][y1][1] == "K":
                    if checkK(x1,y1,x2,y2) == True:
                        board[x2][y2] = board[x1][y1]
                        board[x1][y1] = chr(y1+97)+str(x1+1)
                    else:
                        print("King at", chr(y1+97)+str(x1+1), "cannot move to", str(chr(y2+97)+str(x2+1)))
                elif board[x1][y1][1] == "P":
                    if checkP(x1,y1,x2,y2) == True:
                        board[x2][y2] = board[x1][y1]
                        board[x1][y1] = chr(y1+97)+str(x1+1)
                    else:
                        print("Pawn at", chr(y1+97)+str(x1+1), "cannot move to", str(chr(y2+97)+str(x2+1)))
            else:
                print("There is already", board[x2][y2], "in your destination")
        else:
            print("You are not moving anything")
    else:
        print("There isn't any piece at", board[x1][y1])
            


# Printing Board Function
def drawBoard():
    for i in range(8):
        for j in range(8):
            print(board[7-i][j], end = ' ')
        print()


        
reset()
drawBoard()
