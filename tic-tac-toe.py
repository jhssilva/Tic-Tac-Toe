#The game was 2 players, one with circle(O) and another with cruz(X)
#Conditionals to win: 3 in a row

import random

class Game():
    board = []
    bot_cursor = ""
    player_cursor = ""
    player_nr = 1
    bot_nr = 2
    
    def __init__(self):
        self.board = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]
        self.bot_cursor = ""
        self.player_cursor = ""
    
    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board
        
    def setOnBoardPos(self, pos, nr):
        self.board[pos // 3][pos % 3] = nr
    
    @property
    def showBoard(self):
        for i in range(0,3):
            print("| {} | {} | {} |".format(self.board[i][0], self.board[i][1], self.board[i][2]))
        
    @property
    def chooseCursor(self):
        cursor = "P"
        while (cursor != "X" and cursor != "O"):
            cursor = input("Wich cursor do you want (O, X)? ")
            print("Choose one of the cursors 'O' or 'X'!")
        self.player_cursor = cursor
        
        if(cursor == "X"):
            self.bot_cursor = "O"
        else:
            self.bot_cursor = "X"
    
    def checkPosition(self, pos):
        if (pos > 9 or pos < 0):
            return False
        
        if(self.board[pos // 3][pos % 3] == 0):
            return True
        return False
    
    def checkWin(self, number):
        #conditions of wining
        # For the win to happen, there is needed to have 3 in a row ("1", "2")
        temp = self.board
        result = False
        
        # Lines and column verification
        for i in range(0,3):
            count = 0
            count_column = 0
            for x in range(0,3):
                if temp[i][x] == number: # line verification
                    count += 1
                if temp[x][i] == number: # Colomn verification
                    count_column += 1
            if count == 3 or count_column == 3:
                result = True
                return result
            else:
                count = 0
                count_column = 0    
        
        count_main = 0
        aux = 2
        count_sec = 0
        # Diagonals verification
        for i in range(0,3): 
            if temp[i][i] ==  number: # First diagonal (Main Diagonal)
                count_main += 1
            
            if temp[i][aux] == number: # Secondary diagonal
                count_sec += 1
                
            aux -= 1
                
        if count_main == 3 or count_sec == 3:
            result = True
        
        return result
    
    @property
    def randomPlay(self):
        pos = 0
        while(not self.checkPosition(pos)):
            pos = random.randint(0, 8)
        self.setOnBoardPos(pos, self.bot_nr)
        
    @property
    def checkAvailablePlays(self):
        for i in range(0,9):
            if(self.checkPosition(i)):
                return True
        return False
              
    @property
    def start(self):
        run = True
        turn = random.randint(0,1)
        if(turn == 0):
            print("You go first!")
        else:
            print("Computer has the first choice!")
            self.randomPlay
            
        while(run):
            if(not self.checkAvailablePlays):
                self.showBoard
                print("Tie Game!")
                run = False  
            else:
                option = 0
                asking = True
                self.showBoard
                while(asking):
                    option = int(input("Choose from 1 to 9: "))
                    if(option <= 0 or option >= 10):
                        print("Out of range, choose nother position!")
                    elif(not self.checkPosition(option - 1)):
                        print("Position it's filled, choose another position!")
                        option = 0
                    else:
                        asking = False
                self.setOnBoardPos(option - 1, self.player_nr)
                
                if(self.checkWin(self.player_nr)):
                    print("The Player won!")
                    run = False
                    break
                
                # Check if there is available plays
                if(not self.checkAvailablePlays):
                    self.showBoard
                    print("Tie Game!")
                    run = False
                else:  
                    # Bot time to play
                    self.randomPlay
                
                    #Check Bot win
                    if(self.checkWin(self.bot_nr)):
                        self.showBoard
                        print("The bot won! You will have better luck next time!")
                        run = False
            
        menu()
                
def menu():
    option = 0
    while(option != 3):
        print("1 - New Game")
        print("3 - Exit")
        option = int(input("Option: "))
        handlerMenu(option)

def handlerMenu(option):
    if (option == 1):
        game = Game()
        game.start
    elif (option == 3):
        print("GoodBye")
        exit(0)
    else:
        print("Choose another option")
    


menu()