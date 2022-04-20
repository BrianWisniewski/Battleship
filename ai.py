import random as r
import userInterface as ui
import boardManager as bM


def AISet(board):
    difficulty = 0
    while difficulty not in ["1", "2"]:
        print("1} Easy")
        print("2} Hard")
        difficulty = input("Difficulty? ")

    board = AIPlaceBoats(board)
    return difficulty, board


def AIPlaceBoats(board):
    BoatLength = [5, 4, 3, 3, 2]

    for Length in BoatLength:

        # set up a random coordinate system
        x = r.randint(0, 9)
        y = r.randint(0, 9)
        up = validateAIPlacementInput((x, y, x, y - Length), Length, board)
        down = validateAIPlacementInput((x, y, x, y + Length), Length, board)
        left = validateAIPlacementInput((x, y, x - Length, y), Length, board)
        right = validateAIPlacementInput((x, y, x + Length, y), Length, board)

        while True:

            randomPlace = r.randint(1, 4)

            if randomPlace == 1 and up == True:
                board = bM.placeShip((x, y, x, y - Length), board)
                break
            elif randomPlace == 2 and down == True:
                board = bM.placeShip((x, y, x, y + Length), board)
                break
            elif randomPlace == 3 and left == True:
                board = bM.placeShip((x, y, x - Length, y), board)
                break
            elif randomPlace == 4 and right == True:
                board = bM.placeShip((x, y, x + Length, y), board)
                break
            elif not (up and down and left and right):
                x = r.randint(0, 9)
                y = r.randint(0, 9)
                up = validateAIPlacementInput((x, y, x, y - Length), Length, board)
                down = validateAIPlacementInput((x, y, x, y + Length), Length, board)
                left = validateAIPlacementInput((x, y, x - Length, y), Length, board)
                right = validateAIPlacementInput((x, y, x + Length, y), Length, board)

    return board


def AIGuess(difficulty, AIBoard):

    # guess on easy mode is basically random but without choosing spots it already chose
    if difficulty == "1":
        while True:
            x = r.randint(0, 9)
            y = r.randint(0, 9)

            if AIBoard[y][x] == ".":
                break

        return (x, y)

    # I want it to be extremely difficult for the average battleship player to win


# I kind of stole this from Brian but I needed to make adjustments
def validateAIPlacementInput(cords, shipLength, board):
    x1, y1, x2, y2 = cords

    # variables for checking validity
    boardValidity = True

    for val in cords:
        if val > 9 or val < 0:
            boardValidity = False

    horizontal = y1 == y2
    horizontalLength = abs(x1 - x2) == shipLength

    vertical = x1 == x2
    verticalLength = abs(y1 - y2) == shipLength

    if boardValidity == True:
        verticalShipCheck = checkAIVertically(x1, y1, y2, board)
        horizontalShipCheck = checkAIHorizontally(y1, x1, x2, board)
    else:
        return False

    if horizontal and horizontalLength and boardValidity and horizontalShipCheck:
        return True

    elif vertical and verticalLength and verticalShipCheck and boardValidity:
        return True

    return False


def checkAIHorizontally(y, x1, x2, board):
    smaller = min(x1, x2)
    larger = max(x1, x2)
    for i in range(larger - smaller + 2):
        for t in range(2):
            if board[y - 1 + t][smaller + i - 1] == "x":
                return False

    return True


def checkAIVertically(x, y1, y2, board):
    smaller = min(y1, y2)
    larger = max(y1, y2)
    for i in range(larger - smaller + 2):
        for t in range(2):
            if board[smaller + i - 1][x - 1 + t] == "x":
                return False
    return True
