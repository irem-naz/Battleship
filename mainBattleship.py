import os
import random

shipSize=4
Dim=10
#create board
def createBoard():
  board=[]
  #creating a 2d list
  for row in range(Dim):
    rowlist=[]
    for col in range(Dim):
        rowlist.append(" ")
    board.append(rowlist)
  #printing the dot put board
  for row in range(Dim):
    for col in range(Dim):
      board[row][col]
  return board

#print board
def printBoard(board):
  #MAKING GRIDS TO THE BOARD
  #print the column numbers on top
  print(" ",end="")
  Columns="ABCDEFGHIJ"
  for cols in range(Dim):
    print(" "+Columns[cols],end="")
  #prints the roof grid
  print("\n +"+"-+"*Dim)
  #prints the rest of the grids
  for row in range(Dim):
    print(str(row)+"|",end="")
    for col in range(Dim):
        print(board[row][col]+"|",end="")
    print("\n +"+"-+"*Dim)

def placeShip():
#make shipStr
  shipList=[]
#starting row
#vertical or horzontal?
  orient=random.randint(0,1)
  rows=int(random.randint(0,Dim-shipSize))
  cols=int(random.randint(0,Dim-shipSize))
  if orient==0:
  #horizontal
    for row in range(rows,rows+1):
      for col in range(shipSize):
        shipList.append([rows,cols])
        cols +=1
  else:
    for rows in range(shipSize):
      for col in range(cols,cols+1):
        shipList.append([rows,cols])
        rows += 1
  
  return shipList

  
def main():
  printBoard(createBoard())
  c_board=createBoard()
  shipList=placeShip()
  #ask the player
  cnt=0
  score=0
  while True:
    if cnt == shipSize:
      break
    old_guess=[]
    guess=[]
    old_guess=input("Please choose a coordinate such as A1?\n")
    if ord(old_guess[0])<65 or ord(old_guess[0])>int(65+Dim) or int(old_guess[1])<0 or int(old_guess[1])>int(Dim):
      print("The values are invalid. Please try again. Valid examples include: A1, B2, C5 etc.\n")
      old_guess=[]
      old_guess=input()
    for row in range(1):
      for col in range(1):
        guess.append([int(old_guess[1]),int(ord(old_guess[0])-65)])
    row,col=guess[0][0],guess[0][1]
    #if shiplist contains the guess
    if shipList.__contains__([row,col])==False:
      print("doesnt exist")
      c_board[row][col]="#"
      os.system("clear")
      printBoard(c_board)
      score+=1
    else:
      print("exists")
      c_board[row][col]="X"
      os.system("clear")
      printBoard(c_board)
      cnt+=1
      score+=1
  print("Congrats! You won. Number of tries is", score,end=".")
         
main()




