# Creating Empty Board
board = [[0] * 8 for _ in range(8)]


# Reset Function
def reset():
    global board
    board = [["" for _ in range(8)] for _ in range(8)]
    
    for i in range(8):
        board[i] = [chr(97 + j) + str(i + 1) for j in range(8)]

    pieces = ["R", "N", "B", "Q", "K", "B", "N", "R"]
    for i in range(8):
        board[0][i] = "W" + pieces[i]
        board[7][i] = "B" + pieces[i]
        board[1][i] = "WP"
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


# Converts UCI to indices (x, y)
def indicesFromUCI(algebraic):
    file = algebraic[0]
    rank = algebraic[1]
    x = int(rank) - 1
    y = ord(file) - 97
    return x, y

# Parses UCI move input into indices (x1, y1, x2, y2)
def parseUCI(move_input):
    if len(move_input) != 4:
        raise ValueError("Invalid move input. Must be in the format 'e2e4'.")
    start = move_input[:2]
    end = move_input[2:]
    x1, y1 = indicesFromUCI(start)
    x2, y2 = indicesFromUCI(end)
    return x1, y1, x2, y2


# Checks if a move is valid (True = Valid, False = Invalid)
def isValidMove(x1, y1, x2, y2, turn):
    piece = board[x1][y1]
    destination = board[x2][y2]

    if piece == chr(y1 + 97) + str(x1 + 1):
        print("There isn't any piece at", board[x1][y1])
        return False

    if piece[0] != turn:
        print(f"It's {turn}'s turn. You can't move {piece}.")
        return False

    if abs(x1 - x2) + abs(y1 - y2) == 0:
        print("You are not moving anything")
        return False

    if piece[0] == destination[0]:
        print("There is already", destination, "in your destination")
        return False

    piece_type = piece[1]
    if piece_type == "B" and checkB(x1, y1, x2, y2):
        return True
    elif piece_type == "N" and checkN(x1, y1, x2, y2):
        return True
    elif piece_type == "R" and checkR(x1, y1, x2, y2):
        return True
    elif piece_type == "Q" and checkQ(x1, y1, x2, y2):
        return True
    elif piece_type == "K" and checkK(x1, y1, x2, y2):
        return True
    elif piece_type == "P" and checkP(x1, y1, x2, y2):
        return True
    else:
        print(f"{piece_type} at", chr(y1 + 97) + str(x1 + 1), "cannot move to", chr(y2 + 97) + str(x2 + 1))
        return False

# UCI Format Move Function
def moveUCI(move_input, turn):
    try:
        x1, y1, x2, y2 = parseUCI(move_input)
        if isValidMove(x1, y1, x2, y2, turn):
            movePiece(x1, y1, x2, y2)
            return True
        return False
    except ValueError as e:
        print(e)
        return False

# Move Piece Function
def movePiece(x1, y1, x2, y2):
    board[x2][y2] = board[x1][y1]
    board[x1][y1] = chr(y1 + 97) + str(x1 + 1)

# Printing Board Function with Unicode Characters and Outlines
def drawBoard():
    piece_symbols = {
        "WK": "♔", "WQ": "♕", "WR": "♖", "WB": "♗", "WN": "♘", "WP": "♙",
        "BK": "♚", "BQ": "♛", "BR": "♜", "BB": "♝", "BN": "♞", "BP": "♟"
    }
    print("  a b c d e f g h")
    print(" +----------------+")
    for i in range(8):
        print(f"{8-i}|", end="")
        for j in range(8):
            piece = board[7-i][j]
            if piece in piece_symbols:
                print(piece_symbols[piece], end="")
            else:
                print(" ", end=" ")
        print(f"|{8-i}")
    print(" +----------------+")
    print("  a b c d e f g h")

# Main Game Loop
def main():
    reset()
    drawBoard()
    turn = "W"
    while True:
        move_input = input(f"Enter move for {'White' if turn == 'W' else 'Black'}: ")
        if moveUCI(move_input, turn):
            drawBoard()
            turn = "B" if turn == "W" else "W"

if __name__ == "__main__":
    main()
