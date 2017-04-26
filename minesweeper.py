#Dante DiClemente, Comp 151, 4-19-17, Minesweeper

import random
from random import randint

def game():
    board = grid() #makes grid
    board = random_cell(board) #makes bombs 
    reveal = makereveal() #reveals spots if picked
    board = place_numbers(board)
    numbers = place_numbers(board)
    print_board(board, reveal, numbers) #prints board with revealed 
    while True:
        print("\n")
        y_cord = int(input("Enter an y cordinate: ")) 
        x_cord = int(input("Enter an x cordinate: "))
        reveal[y_cord][x_cord] = "true"
        if (board[y_cord][x_cord] == '*'):
            print("\n")
            print("BOOM!") #if you pick a bomb the game ends
            break
        else:
            print_board(board, reveal, numbers)

###########################################

def grid():
    row = [] #creates grid 
    for i in range(10):
        row.append([","]*10)

    return(row)

############################################

def makereveal(): #used to reveal tiles
    row = []
    for i in range(10):
        row.append(["false"]*10)

    return(row)

############################################

def random_cell(board): #imports bombs into the grid
    for j in range(10):
        for i in range(10):
         if (random.random() < 0.1):
            board[j][i] = "*"

    return(board)
                
############################################

def print_board(random_cell, reveal, numbers):
    for y in range(10): 
        print("")
        for x in range(10): #prints board in special format to look like a board
            if(reveal[y][x] == "false"):
                print("x", end="")
            elif(reveal[y][x] == "true"):
                num = numbers[y][x]
                print(num, end="")

    return("")

############################################

def place_numbers(board):
    for y in range(9):
        for x in range(9): #checks for all mines surrounding spot
            minecount = 0
            if board[y][x] == "*":
                board[y][x] = "*"
            #Left
            if(board[y][x-1] == "*" and x != 0):
                 minecount += 1
                 board[y][x] = minecount
            #Right
            if(board[y][x+1] == "*" and x != 9):
                 minecount += 1
                 board[y][x] = minecount
            #Up
            if(board[y-1][x] == "*" and y != 0):
                 minecount += 1
                 board[y][x] = minecount
            #Down
            if(board[y+1][x] == "*" and y != 9):
                 minecount += 1
                 board[y][x] = minecount
            #Top left
            if(board[y+1][x-1] == "*" and y != 0 and x != 0):
                 minecount += 1
                 board[y][x] = minecount
            #Top Right
            if(board[y-1][x+1] == "*" and y != 0 and x != 9):
                 minecount += 1
                 board[y][x] = minecount
            #Bottom Left
            if(board[y-1][x-1] == "*" and x != 0 and y != 9):
                 minecount += 1
                 board[y][x] = minecount
            #Bottom Right
            if(board[y+1][x+1] == "*" and y != 9 and x != 9):
                 minecount += 1
                 board[y][x] = minecount                 
                 
    for column in range(10):
        for row in range(10):
            if board[column][row] == ",": #replaces commas with zeros
                board[column][row] = 0
        
    return(board)
