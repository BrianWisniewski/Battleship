import typing


# Checks to ensure there is not a horiontal ship overlapping
# with the coordinates given. Returns True if valid and False otherwise.
def checkHorizontally(y: int, x1: int, x2: int, board: list) -> bool:
    smaller = min(x1, x2)
    larger = max(x1, x2)
    tmpList = board[y][smaller : larger + 1]
    if "x" in tmpList:
        return False
    return True


# Checks to ensure there is not a vertical ship overlapping
# with the coordinates given. Returns True if valid and Fase otherwise.
def checkVertically(x: int, y1: int, y2: int, board: list) -> bool:
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
def validateUserPlacementInput(cords: tuple, shipLength: int, board: list) -> bool:
    x1, y1, x2, y2 = cords

    print(x1, y1, x2, y2)
    if x1 == x2:
        if abs(y1 - y2) == shipLength and False not in (0 <= val <= 9 for val in cords):
            if checkVertically(x1, y1, y2, board):
                return True
    elif y1 == y2:
        if abs(x1 - x2) == shipLength and False not in (0 <= val <= 9 for val in cords):
            if checkHorizontally(y1, x1, x2, board):
                return True
    return False


# Checks to ensure a cannon shot is on the board and has not already been
# shot at by the user.
def validateUserShot(x: int, y: int) -> bool:
    ##TODO: add checking for already shot at coordinates
    if 0 <= x <= 9 and 0 <= y <= 9:
        print("Your point is not on the board.")
        return True
    return False


def getXYCords(point: str) -> tuple:
    x1 = ord(point[0].upper()) - 65
    y1 = int(point[1] - 1)
    return (x1, y1)


def getUserShips(board):
    print(
        "To play the game you must first place your ships. Each player has one 2 grid ship, two 3 grid ships, one 4 grid ship, and one 5 grid ship."
    )
    print(
        "To place your ships, you will enter the starting and ending coordinates of each ship when prompted. Ex: A3"
    )
    userPrompt = [
        ("first", 5),
        ("second", 3),
        ("third", 3),
        ("fourth", 4),
        ("fifth", 5),
    ]
    for order, length in userPrompt:
        valid = False
        while valid is False:
            starting = getXYCords(
                input(
                    f"Please enter the starting coordinate of your {order} ship with length {length}. Ex: A3"
                )
            )
            ending = getXYCords(
                input(
                    f"Please enter the ending coordinate of your {order} ship with length {length}. Ex: C3"
                )
            )
            cords = starting + ending
            valid = validateUserPlacementInput(cords, length, board)
            if not valid:
                print("One or more of your cordinates are invalid.")


print()
