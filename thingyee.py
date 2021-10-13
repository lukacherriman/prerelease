#Skeleton Program for the AQA COMP1 Summer 2016 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA COMP1 Programmer Team
#developed in a Python 3.4 programming environment

import math
import random

"gets up the satrting pieces of the game"
def SetUpGameBoard(Board, Boardsize):
  setup = ""
  while setup != "inner" and setup != "outer":
    setup = input("enter middle or inner for the board setup: ")

  if setup == "inner":
    for Row in range(1, BoardSize + 1):
      for Column in range(1, BoardSize + 1):
        if (Row == (BoardSize + 1) // 2 and Column == (BoardSize + 1) // 2 + 1) or (Column == (BoardSize + 1) // 2 and Row == (BoardSize + 1) // 2 + 1):
          Board[Row][Column] = "C"
        elif (Row == (BoardSize + 1) // 2 + 1 and Column == (BoardSize + 1) // 2 + 1) or (Column == (BoardSize + 1) // 2 and Row == (BoardSize + 1) // 2):
          Board[Row][Column] = "H"
        else:
          Board[Row][Column] = " "
  elif setup == "outer":
    for Row in range(1, BoardSize + 1):
      for Column in range(1, BoardSize + 1):
          Board[Row][Column] = " "
    Board[1][1] = "H"
    Board[1][BoardSize] = "C"
    Board[BoardSize][1] = "H"
    Board[BoardSize][BoardSize] = "C"

"gets the board size input from the player"
def ChangeBoardSize():
  BoardSize = int(input("Enter a board size (between 4 and 9): "))
  while not(BoardSize >= 4 and BoardSize <= 9):
    BoardSize = int(input("Enter a board size (between 4 and 9): "))
  return BoardSize


"gets the move input from the player"
def GetHumanPlayerMove(PlayerName):
  integer = False
  while integer == False:
    print(PlayerName, "enter the coodinates of the square where you want to place your piece: ", end="")
    try:
      Coordinates = int(input())
      integer  = True
    except:
      integer  = False

  return Coordinates


"gets the random move from the computer "
def GetComputerPlayerMove(BoardSize):
  return random.randint(1, BoardSize) * 10 + random.randint(1, BoardSize)


"checks if the game is over returns true of false"
def GameOver(Board, BoardSize):
  for Row in range(1 , BoardSize + 1):
    for Column in range(1, BoardSize + 1):
      if Board[Row][Column] == " ":
        return False
  return True


"function gets an input of the players name"
def GetPlayersName():
  PlayerName = input("What is your name? ")
  return PlayerName


"function called within PlayGame checks if the move made is valid or already has a piece there "
def CheckIfMoveIsValid(Board, Move, BoardSize):
  if int(Move) != Move:
    return False
  Row = Move % 10
  Column = Move // 10
  MoveIsValid = False
  if Row > BoardSize or Column > BoardSize:
    MoveIsValid = False
  elif Board[Row][Column] == " ":
    MoveIsValid = True
  return MoveIsValid


"function gets the score of "
def GetPlayerScore(Board, BoardSize, Piece):
  Score = 0
  for Row in range(1, BoardSize + 1):
    for Column in range(1, BoardSize + 1):
      if Board[Row][Column] == Piece:
        Score = Score + 1
  return Score


"called within flip opponen pieces, checks if there are pieces valid to be flipped"
def CheckIfThereArePiecesToFlip(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection):
  RowCount = StartRow + RowDirection
  ColumnCount = StartColumn + ColumnDirection
  FlipStillPossible = True
  FlipFound = False
  OpponentPieceFound = False
  while RowCount <= BoardSize and RowCount >= 1 and ColumnCount >= 1 and ColumnCount <= BoardSize and FlipStillPossible and not FlipFound:
    if Board[RowCount][ColumnCount] == " ":
      FlipStillPossible = False
    elif Board[RowCount][ColumnCount] != Board[StartRow][StartColumn]:
      OpponentPieceFound = True
    elif Board[RowCount][ColumnCount] == Board[StartRow][StartColumn] and not OpponentPieceFound:
      FlipStillPossible = False
    else:
      FlipFound = True
    RowCount = RowCount + RowDirection
    ColumnCount = ColumnCount + ColumnDirection
  return FlipFound


"a function called within MakeMove flips the players piece to the other players if they are between two pieces "
def FlipOpponentPiecesInOneDirection(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection):
  FlipFound = CheckIfThereArePiecesToFlip(Board, BoardSize, StartRow, StartColumn, RowDirection, ColumnDirection)
  if FlipFound:
    RowCount = StartRow + RowDirection
    ColumnCount = StartColumn + ColumnDirection
    while Board[RowCount][ColumnCount] != " " and Board[RowCount][ColumnCount] != Board[StartRow][StartColumn]:
      if Board[RowCount][ColumnCount] == "H":
        Board[RowCount][ColumnCount] = "C"
      else:
        Board[RowCount][ColumnCount] = "H"
      RowCount = RowCount + RowDirection
      ColumnCount = ColumnCount + ColumnDirection


"takes the players input and converts it into a column and a row places that piece and then runs th flip piece function"
def MakeMove(Board, BoardSize, Move, HumanPlayersTurn):
  Row = Move % 10
  Column = Move // 10
  if HumanPlayersTurn:
    Board[Row][Column] = "H"
  else:
    Board[Row][Column] = "C"
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 1, 0)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, -1, 0)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 0, 1)
  FlipOpponentPiecesInOneDirection(Board, BoardSize, Row, Column, 0, -1)


"a function called within the DisplayGameBoard function prints the lines between each row"
def PrintLine(BoardSize):
  print("   ", end="")
  for Count in range(1, BoardSize * 2):
    print("_", end="")
  print()


"function displays the board in the output"
def DisplayGameBoard(Board, BoardSize):
  print()
  print("  ", end="")
  for Column in range(1, BoardSize + 1):
    print(" ", end="")
    print(Column, end="")
  print()
  PrintLine(BoardSize)
  for Row in range(1, BoardSize + 1):
    print(Row, end="")
    print(" ", end="")
    for Column in range(1, BoardSize + 1):
      print("|", end="")
      print(Board[Row][Column], end="")
    print("|")
    PrintLine(BoardSize)
    print()


"function prints the options for the input menu"
def DisplayMenu():
  print("(p)lay game")
  print("(e)nter name")
  print("(c)hange board size")
  print("(q)uit")
  print()


"function gets the players input into the game and returns their move"
def GetMenuChoice(PlayerName):
  print(PlayerName, "enter the letter of your chosen option: ", end="")
  Choice = input()
  return Choice


"this function creates the game board to the size given"
def CreateBoard():
  Board = []
  for Count in range(BoardSize + 1):
    Board.append([])
    for Count2 in range(BoardSize + 1):
      Board[Count].append("")
  return Board


def PlayGame(PlayerName, BoardSize):
  Board = CreateBoard()
  SetUpGameBoard(Board, BoardSize)
  HumanPlayersTurn = False
  while not GameOver(Board, BoardSize):
    HumanPlayersTurn = not HumanPlayersTurn
    DisplayGameBoard(Board, BoardSize)
    MoveIsValid = False
    while not MoveIsValid:
      if HumanPlayersTurn:
        Move = GetHumanPlayerMove(PlayerName)
      else:
        Move = GetComputerPlayerMove(BoardSize)
      MoveIsValid = CheckIfMoveIsValid(Board, Move, BoardSize)
    if not HumanPlayersTurn:
      print("Press the Enter key and the computer will make its move")
      input()
    MakeMove(Board, BoardSize, Move, HumanPlayersTurn)
  DisplayGameBoard(Board, BoardSize)
  HumanPlayerScore = GetPlayerScore(Board, BoardSize, "H")
  ComputerPlayerScore = GetPlayerScore(Board, BoardSize, "C")
  if HumanPlayerScore > ComputerPlayerScore:
    print("Well done", PlayerName, ", you have won the game!")
  elif HumanPlayerScore == ComputerPlayerScore:
    print("That was a draw!")
  else:
    print("The computer has won the game!")
  print()


"""this part of the code initialises the original variables used in the code and then begins a loop to the players 
input for what they would like to run breaking when the player inputs q for the other inputs it will run certain 
functions"""
random.seed()
BoardSize = 6
PlayerName = ""
Choice = ""
while Choice != "q":
  DisplayMenu()
  Choice = GetMenuChoice(PlayerName)
  if Choice == "p":
    PlayGame(PlayerName, BoardSize)
  elif Choice == "e":
    PlayerName = GetPlayersName()
  elif Choice == "c":
    BoardSize = ChangeBoardSize()