import random as r
import userInterface as ui
import boardManager as bm
import ai

p1Board = bm.generateBoard()
p1ShipBoard = bm.generateBoard()
p2Board = bm.generateBoard()
p2ShipBoard = bm.generateBoard()


def start():
    global p1ShipBoard
    player = 0
    while player != "1" and player != "2":
        print("1} Single Player")
        print("2} 2 Player")
        player = input("1 or 2 Player Battleship: ")

    if player == "1":
        # playerSet()
        aiDifficulty, aiBoard = ai.AISet(p2ShipBoard)
        bm.printBoard(aiBoard, "Computer")


start()
