import random

# Generates a fresh battleship board
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


# Displays the board to the user
def printBoard(board, message):
    print(message.center(31, " "))
    print("   A  B  C  D  E  F  G  H  I  J")
    for index, line in enumerate(board):
        print(str(index + 1).ljust(3, " "), end="")
        for value in line:
            print(f"{value} ", end=" ")
        print("\n")


# Adds a ship to the board at the coordinates given
def placeShip(cordinates, board):
    x1, y1, x2, y2 = cordinates

    horizontal = y1 == y2
    vertical = x1 == x2

    if horizontal:
        Xmax = max(x1, x2)
        Xmin = min(x1, x2)
        for i in range(Xmax - Xmin + 1):
            board[y1][Xmin + i] = "x"
    elif vertical:
        Ymax = max(y1, y2)
        Ymin = min(y1, y2)
        for i in range(Ymax - Ymin + 1):
            board[Ymin + i][x1] = "x"

    return board


# Takes a shot at the given coordinates and prints hit or miss to the user
def shoot(x, y, shipBoard, hitBoard):
    print("Shot at " + chr(x + 65) + str(y + 1) + ":")
    if shipBoard[y][x] == "x":
        print("Hit!")
        hitBoard[y][x] = "x"
    else:
        print("Miss!")
        hitBoard[y][x] = "o"
    return hitBoard


# Checks if someone has won the game. Returns True if someone has won and False otherwise
def checkWin(board):
    hitCounter = 0
    for line in board:
        for item in line:
            if item == "x":
                hitCounter += 1
    if hitCounter >= 17:
        return True
    return None


# Checks to ensure there is not a horiontal ship overlapping
# with the coordinates given. Returns True if valid and False otherwise.
def checkHorizontally(y, x1, x2, board):
    smaller = min(x1, x2)
    larger = max(x1, x2)
    tmpList = board[y][smaller : larger + 1]
    if "x" in tmpList:
        return False
    return True


# Checks to ensure there is not a vertical ship overlapping
# with the coordinates given. Returns True if valid and Fase otherwise.
def checkVertically(x, y1, y2, board):
    smaller = min(y1, y2)
    larger = max(y1, y2)
    tmpList = []
    for i, line in enumerate(board):
        if i in range(smaller, larger + 1):
            tmpList.append(line[x])
    if "x" in tmpList:
        return False
    return True


# Checks to ensure a user placed ship is valid. Returns True if valid and False otherwise
# Ships are valid if they do not overlap with other ships, are on the board,
# have the correct length, and are either horizontal or vertical.
def validatePlacement(cords, shipLength, board):
    x1, y1, x2, y2 = cords

    if x1 == x2:
        if abs(y1 - y2) == shipLength - 1 and False not in (
            0 <= val <= 9 for val in cords
        ):
            if checkVertically(x1, y1, y2, board):
                return True
    elif y1 == y2:
        if abs(x1 - x2) == shipLength - 1 and False not in (
            0 <= val <= 9 for val in cords
        ):
            if checkHorizontally(y1, x1, x2, board):
                return True
    return False


# Checks to ensure a cannon shot is on the board and has not already been
# shot at by the user.
def validateShot(x, y, hitBoard, silent=False):
    try:
        if hitBoard[y][x] == "x" or hitBoard[y][x] == "o":
            if silent is False:
                print("That move has already been made.")
            return False

        elif not (0 <= x <= 9 and 0 <= y <= 9):
            if silent is False:
                print("Your point is not on the board.")
                print('Coordinates should be entered as "row column"')
                print("ie: A 1, B 2 or F 7")
            return False
    except:
        return False
    return True


# Converts a user entered string into a integer coordinate pair
def getXYCords(point):
    try:
        x1 = ord(point[0].upper()) - 65
        y1 = int(point[1:]) - 1
    except:
        return (11, 11)
    return (x1, y1)


# Gets the player ready to start playing the game
# This includes placing the ships and displaying the board
def getUserShips(board):
    print("To play the game you must first place your ships.")
    print("Each player has one 2 grid ship, two 3 grid ships,")
    print("one 4 grid ship, and one 5 grid ship.\n")
    print("To place your ships, you will enter the starting and")
    print("ending coordinates of each ship when prompted. Ex: A3\n")
    userPrompt = [
        ("first", 5),
        ("second", 4),
        ("third", 3),
        ("fourth", 3),
        ("fifth", 2),
    ]
    for order, length in userPrompt:
        valid = False
        while valid is False:
            printBoard(board, "Ship Board")
            print(f"Enter the coordinates of your {order} ship with length {length}")
            starting = getXYCords(input("Starting: "))
            ending = getXYCords(input("Ending: "))
            cords = starting + ending
            valid = validatePlacement(cords, length, board)
            if not valid:
                print("One or more of your cordinates are invalid.")

        board = placeShip(cords, board)
    printBoard(board, "Your Ships")
    return board


# Generates random coordinates for the ai to shoot at and ensures
# the shot has not alreay been taken.
# This function was written by my partner.
def AIGuess(AIHitBoard):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        if AIHitBoard[y][x] == ".":
            break

    return (x, y)


# Ensures an AI ship is valid
# This function was written by my partner.
def validateAIPlacement(cords, shipLength, board):
    x1, y1, x2, y2 = cords

    for val in cords:
        if val > 9 or val < 0:
            return False

    horizontal = y1 == y2
    horizontalLength = abs(x1 - x2) == shipLength

    vertical = x1 == x2
    verticalLength = abs(y1 - y2) == shipLength

    verticalShipCheck = checkVertically(x1, y1, y2, board)
    horizontalShipCheck = checkHorizontally(y1, x1, x2, board)

    if horizontal and horizontalLength and horizontalShipCheck:
        return True

    elif vertical and verticalLength and verticalShipCheck:
        return True

    return False


# Sets up the AI's ships and returns the set up board
# This function was written by my partner.
def AIPlaceBoats():
    board = generateBoard()
    BoatLength = [4, 3, 2, 2, 1]

    for Length in BoatLength:

        # set up a random coordinate system
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        up = validateAIPlacement((x, y, x, y - Length), Length, board)
        down = validateAIPlacement((x, y, x, y + Length), Length, board)
        left = validateAIPlacement((x, y, x - Length, y), Length, board)
        right = validateAIPlacement((x, y, x + Length, y), Length, board)

        while True:

            randomPlace = random.randint(1, 4)

            if randomPlace == 1 and up == True:
                board = placeShip((x, y, x, y - Length), board)
                break
            elif randomPlace == 2 and down == True:
                board = placeShip((x, y, x, y + Length), board)
                break
            elif randomPlace == 3 and left == True:
                board = placeShip((x, y, x - Length, y), board)
                break
            elif randomPlace == 4 and right == True:
                board = placeShip((x, y, x + Length, y), board)
                break
            elif not (up and down and left and right):
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                up = validateAIPlacement((x, y, x, y - Length), Length, board)
                down = validateAIPlacement((x, y, x, y + Length), Length, board)
                left = validateAIPlacement((x, y, x - Length, y), Length, board)
                right = validateAIPlacement((x, y, x + Length, y), Length, board)

    return board


print("LET'S PLAY BATTLESHIP!\n\n")

# set ai boards
aiHitBoard = generateBoard()
aiShipBoard = AIPlaceBoats()

# set player boards
userHitBoard = generateBoard()
userShipBoard = getUserShips(generateBoard())

# main game loop
winner = None
while winner is None:

    # get and validate user shot
    validShot = False
    while validShot == False:
        xShot, yShot = (0, 0)
        userShot = input("Enter the location to hit: ")
        userShot = "".join(userShot.split())
        userXShot, userYShot = getXYCords(userShot)
        validShot = validateShot(userXShot, userYShot, userHitBoard)
    # take the valid user shot
    userHitBoard = shoot(userXShot, userYShot, aiShipBoard, userHitBoard)
    printBoard(userHitBoard, "Your Shots")

    # check if the player has won
    winner = checkWin(userHitBoard)
    if winner is not None:
        winner = "player"
        break

    # take valid ai shot
    aiXShot, aiYShot = AIGuess(aiHitBoard)
    aiHitBoard = shoot(aiXShot, aiYShot, userShipBoard, aiHitBoard)
    printBoard(aiHitBoard, "AI Shots")
    # check if the ai has won
    winner = checkWin(aiHitBoard)
    if winner is not None:
        winner = "ai"
        break

print("\nGame Over!\n")
if winner == "player":
    print("You win!")
elif winner == "ai":
    print("You lost to the computer!")
