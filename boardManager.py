def generateBoard():
    board = [
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
    return board
    # Shot board:
    #   hit - x
    #   miss - O
    #   not shot - .

    # Ship board:
    #   ship - X
    #   water - .


def printBoard(board, player):
    print(player.center(22, " "))
    print("   A B C D E F G H I J")
    for index, line in enumerate(board):
        print(str(index + 1).ljust(3, " "), end="")
        for value in line:
            print(f"{value} ", end="")
        print("\n")


# Noah's Code
def placeShip(cordinates, board):
    x1, y1, x2, y2 = cordinates

    horizontal = y1 == y2
    vertical = x1 == x2

    if horizontal:
        Xmax = max(x1, x2)
        Xmin = min(x1, x2)
        for i in range(Xmax - Xmin):
            board[y1][Xmin + i] = "x"
    elif vertical:
        Ymax = max(y1, y2)
        Ymin = min(y1, y2)
        for i in range(Ymax - Ymin):
            board[Ymin + i][x1] = "x"

    return board
