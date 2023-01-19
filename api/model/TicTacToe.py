#create a game of TicTacToe
import random


class TicTacToe:
    def __init__(self,player1,computer,id):
        self.player1=player1
        self.computer=computer
        self.board=[['0','0','0'],['0','0','0'],['0','0','0']]
        self.winner=None
        self.turn=0
        self.gameOver=False 
        self.id=id

    def printBoard(self):
        for i in range(3):
            print(self.board[i])
            for j in range(3):
                print(self.board[i][j],end=" ")
    
    def checkWinner(self):
        for i in range(3):
            if self.board[i][0]==self.board[i][1]==self.board[i][2] and self.board[i][0]!=' ':
                self.winner=self.board[i][0]
                self.gameOver=True
                return True
            if self.board[0][i]==self.board[1][i]==self.board[2][i] and self.board[0][i]!=' ':
                self.winner=self.board[0][i]
                self.gameOver=True
                return True
        if self.board[0][0]==self.board[1][1]==self.board[2][2] and self.board[0][0]!=' ':
            self.winner=self.board[0][0]
            self.gameOver=True
            return True
        if self.board[0][2]==self.board[1][1]==self.board[2][0] and self.board[0][2]!=' ':
            self.winner=self.board[0][2]
            self.gameOver=True
            return True
        return False
    
    def checkDraw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j]==' ':
                    return False
        self.gameOver=True
        return True
    
    def play(self):
        while not self.gameOver:
            self.printBoard()
            if self.turn%2==0:
                self.player1.makeMove(self.board)
            else:
                self.computer.makeMove(self.board)
            self.turn+=1
            if self.checkWinner():
                self.printBoard()
                print("Winner is",self.winner)
            elif self.checkDraw():
                self.printBoard()
                print("Draw")

class player:
    def __init__(self,player):
        self.player=player
    
    def makeMove(self,board):
        print("Player",self.player,"turn")
        while True:
            x=int(input("Enter x coordinate: "))
            y=int(input("Enter y coordinate: "))
            if board[x][y]==' ':
                board[x][y]=self.player
                break
            else:
                print("Invalid move")

class computer:
    def __init__(self,player):
        self.player=player
    
    def makeMove(self,board):
        print("Computer turn")
        while True:
            x=random.randint(0,2)
            y=random.randint(0,2)
            if board[x][y]==' ':
                board[x][y]=self.player
                break
            else:
                continue