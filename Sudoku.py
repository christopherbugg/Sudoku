__author__ = 'ChrisBugg'
#   Sudoku.py

#   A program to solve "easy" Sudoku puzzles
#   version Nov. 8, 2007, revised January 2010

#   Originally by Jerry Hammond? (COSC 1010 @uwyo.edu) in Java
#   Re-written, modified, and upgraded by Chris Bugg in Python3

#   Created: 5/19/14
#   Modified: 5/22/14

#Imports
import os

#Sudoku Class
class Sudoku():

    #Class Variables
    problem = [[0, 0, 4,   0, 0, 0,   0, 6, 7], [3, 0, 0,   4, 7, 0,   0, 0, 5], [1, 5, 0,   8, 2, 0,   0, 0, 3], [0, 0, 6,   0, 0, 0,   0, 3, 1], [8, 0, 2,   1, 0, 5,   6, 0, 4], [4, 1, 0,   0, 0, 0,   9, 0, 0], [7, 0, 0,   0, 8, 0,   0, 4, 6], [6, 0, 0,   0, 1, 2,   0, 0, 0], [9, 3, 0,   0, 0, 0,   7, 1, 0]]
    #Empty puzzle
    empty = [[0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0, 0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0]]
    #For Printing
    tempProblem = [[0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0], [0, 0, 0,   0, 0, 0,   0, 0, 0]]

    #Constructor
    def __init__(self):

        #Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        self.intro()

        #Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        #Get their choice
        print("Are you looking to import from a file (type 'file') ")
        print("     or input by hand (type 'key')? ")
        choice = input()

        #Sterolize Inputs
        goodNames = {"file", "key"}

        while not choice in goodNames:

            print("Input Error!")

            choice = input("Try Again: ")

        #Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        if choice == "file":

            self.importIt()

        else:

            self.keyIt()

        #Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        print("So here's your puzzle.")

        self.printItNew()

        exit = input("Ready to solve? (Press Enter) ")

        print("Solving...")

        self.solveOne()

        print("Done Solving. Puzzle: ")

        self.printItNew()

        exit = input("Done? (Press Enter) ")

        print("Done.")

    #Intro screen
    def intro(self):

        print("+------------+------------+------------+")
        print("|  .   .   . |  .   .   . |  .   7   1 | ")
        print("|  .   .   . |  5   6   . |  3   4   8 | ")
        print("|  .   .   8 |  .   3   . |  6   5   . | ")
        print("+------------+S U D O K U-+------------+")
        print("|  .   6   . |  .   .   4 |  .   .   3 | ")
        print("|  .   8   2 |  .   .   . |  1   6   . | ")
        print("|  3   .   . |  6   .   . |  .   2   . | ")
        print("+------------+-S O L V E R+------------+")
        print("|  .   4   3 |  .   9   . |  2   .   . | ")
        print("|  1   9   7 |  .   2   6 |  .   .   . | ")
        print("|  8   2   . |  .   .   . |  .   .   . | ")
        print("+----PRESS---+------------+----ENTER---+")

        exit = input()

    #Imports file and processes
    def importIt(self):

        print("Just so you know, the format for the file")
        print(" should look something like this:")
        print("8 6 1 0 4 7 0 9 0")
        print(" where each line is a new row.")
        print()

        fileName = input("What's the name of the .txt (text) file: ") + ".txt"

        file = open(fileName, 'r')

        #Put all lines into a list
        allList = list(file)

        counter = 0

        for x in allList:

            #Split the line from string to list
            lineList = x.split()

            lineList.reverse()

            for y in range(0, 9):

                self.problem[counter][y] = int(lineList.pop())

            counter += 1

    #Allows user to key in puzzle
    def keyIt(self):

        self.problem = self.empty

        print("Okay, lets go one row at-a-time.")
        print("Enter the first row, and hit 'Enter',")
        print(" then the next until you've got it all")
        print("Note: '0's are for blank spaces, and leave")
        print("one space between numbers.")
        print()

        for row in range(0, 9):

            print("Here's what we've got so far:")
            self.printItNew()

            lineList = input().split()

            lineList.reverse()

            for col in range(0, 9):

                self.problem[row][col] = int(lineList.pop())

            #Clear screen
            os.system('cls' if os.name == 'nt' else 'clear')



    #Solves this Sudoku problem
    def solveOne(self):

        if not self.solveTwo(0, 0):

            print("No Solution Possible!")

    #Recursively solves this Sudoku problem
    def solveTwo(self, row, col):

        #Go to next row if at the end
        if col >= 9:

            row += 1
            col = 0

        #If all spaces are filled, then the puzzle is solved
        if row >= 9:

            print("Solved!")

            return True

        #If the space is marked, go to the next one
        if 0 != self.problem[row][col]:

            return self.solveTwo(row, col + 1)

        else:

            #Try all possible numbers
            solved = False

            for i in range(1, 10):

                if self.isPossibleDigit(i, row, col):

                    #Mark it and recurse on the next box
                    self.problem[row][col] = i

                    solved = self.solveTwo(row, col + 1)

                    #If this isn't a solution...
                    if solved == False:

                        #Unmark it after recursing
                        self.problem[row][col] = 0

            return solved

    #Prints the 9x9 array (problem) as a Sudoku board.
    def printItNew(self):

        for row in range(0, 9):

            for col in range(0, 9):

                if self.problem[row][col] == 0:

                    self.tempProblem[row][col] = "."

                else:

                    self.tempProblem[row][col] = self.problem[row][col]

        print("+------------+------------+------------+")
        print("| ", self.tempProblem[0][0], " ", self.tempProblem[0][1], " ", self.tempProblem[0][2], "| ", self.tempProblem[0][3], " ", self.tempProblem[0][4], " ", self.tempProblem[0][5], "| ", self.tempProblem[0][6], " ", self.tempProblem[0][7], " ", self.tempProblem[0][8], "| ")
        print("| ", self.tempProblem[1][0], " ", self.tempProblem[1][1], " ", self.tempProblem[1][2], "| ", self.tempProblem[1][3], " ", self.tempProblem[1][4], " ", self.tempProblem[1][5], "| ", self.tempProblem[1][6], " ", self.tempProblem[1][7], " ", self.tempProblem[1][8], "| ")
        print("| ", self.tempProblem[2][0], " ", self.tempProblem[2][1], " ", self.tempProblem[2][2], "| ", self.tempProblem[2][3], " ", self.tempProblem[2][4], " ", self.tempProblem[2][5], "| ", self.tempProblem[2][6], " ", self.tempProblem[2][7], " ", self.tempProblem[2][8], "| ")
        print("+------------+------------+------------+")
        print("| ", self.tempProblem[3][0], " ", self.tempProblem[3][1], " ", self.tempProblem[3][2], "| ", self.tempProblem[3][3], " ", self.tempProblem[3][4], " ", self.tempProblem[3][5], "| ", self.tempProblem[3][6], " ", self.tempProblem[3][7], " ", self.tempProblem[3][8], "| ")
        print("| ", self.tempProblem[4][0], " ", self.tempProblem[4][1], " ", self.tempProblem[4][2], "| ", self.tempProblem[4][3], " ", self.tempProblem[4][4], " ", self.tempProblem[4][5], "| ", self.tempProblem[4][6], " ", self.tempProblem[4][7], " ", self.tempProblem[4][8], "| ")
        print("| ", self.tempProblem[5][0], " ", self.tempProblem[5][1], " ", self.tempProblem[5][2], "| ", self.tempProblem[5][3], " ", self.tempProblem[5][4], " ", self.tempProblem[5][5], "| ", self.tempProblem[5][6], " ", self.tempProblem[5][7], " ", self.tempProblem[5][8], "| ")
        print("+------------+------------+------------+")
        print("| ", self.tempProblem[6][0], " ", self.tempProblem[6][1], " ", self.tempProblem[6][2], "| ", self.tempProblem[6][3], " ", self.tempProblem[6][4], " ", self.tempProblem[6][5], "| ", self.tempProblem[6][6], " ", self.tempProblem[6][7], " ", self.tempProblem[6][8], "| ")
        print("| ", self.tempProblem[7][0], " ", self.tempProblem[7][1], " ", self.tempProblem[7][2], "| ", self.tempProblem[7][3], " ", self.tempProblem[7][4], " ", self.tempProblem[7][5], "| ", self.tempProblem[7][6], " ", self.tempProblem[7][7], " ", self.tempProblem[7][8], "| ")
        print("| ", self.tempProblem[8][0], " ", self.tempProblem[8][1], " ", self.tempProblem[8][2], "| ", self.tempProblem[8][3], " ", self.tempProblem[8][4], " ", self.tempProblem[8][5], "| ", self.tempProblem[8][6], " ", self.tempProblem[8][7], " ", self.tempProblem[8][8], "| ")
        print("+------------+------------+------------+")

    #Returns a 3x3 array representing a "box" of the 9x9 array.
    # The params boxRow and boxColumn are in the range 0 to 2
    # since there are three rows and three columns of "boxes."
    def getBox(self, boxRow, boxColumn):

        box = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        if (boxRow <= 2) and (boxColumn <= 2):

            rowOffset = int(boxRow * 3)
            colOffset = int(boxColumn * 3)

            for row in range(0, 3):

                for col in range(0, 3):

                    box[row][col] = self.problem[rowOffset + row][colOffset + col]

        return box

    #Returns true if the given digit (which must be 1..9) occurs
    # in the given row (rows are 0...8), and false otherwise.
    def occursInRow(self, digit, row):

        for col in range(0, 9):

            if self.problem[row][col] == digit:

                return True

        return False

    #Returns true if the given digit (which must be 1..9) occurs
    # in the given column (columns are 0..8) and false otherwise.
    def occursInColumn(self, digit, column):

        for row in range(0, 9):

            if self.problem[row][column] == digit:

                return True

        return False

    #Returns true if the given digit (which must be 1..9) occurs
    # in the given box, and flase otherwise.
    def occursInBox(self, digit, box):

        for row in range(0, 3):

            for col in range(0, 3):

                if box[row][col] == digit:

                    return True

        return False

    #Returns true if the given digit (which must be 1..9) occurs in the box
     # containing the location at the given row and column of the 9x9 array, and
     # false otherwise. Note that this function is given a row and column in the
     # complete 9x9 array, but must search for the given digit in the box containing
     # that (row, column) location.
    def occursInBoxTwo(self, digit, row, column):

        if row <= 2:

            boxRow = 0

        elif row >= 6:

            boxRow = 2

        else:

            boxRow = 1

        if column <= 2:

            boxCol = 0

        elif column >= 6:

            boxCol = 2

        else:

            boxCol = 1

        return self.occursInBox(digit, self.getBox(boxRow, boxCol))

    #Returns true if the given digit (which must be 1..9) does not occur in the
     # given row, or in the given column, or in the box containing this row and
     # column, and false otherwise. That is, this digit is a possible candidate for
     # putting in this location; there may be other candidates.
    def isPossibleDigit(self, digit, row, column):

        if self.occursInRow(digit, row) == True:

            return False

        elif self.occursInColumn(digit, column) == True:

            return False

        elif self.occursInBoxTwo(digit, row, column) == True:

            return False

        else:

            return True
Sudoku()