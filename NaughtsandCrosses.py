#Initialising game
board = ["-", "-", "-","-", "-", "-","-", "-", "-"]

print("Welcome to Noughts and Crosses!")
p1=input("Enter Player 1's Name: ")
p2=input("Enter Player 2's Name: ")

#Global variables
winner=None
current_player="X"
word_current_player=p1
game_still_going = True

def display_board():
        print("Current Board:")
        print("|" + board[0]+"|" + board[1]+"|" + board[2]+"|")
        print("|" + board[3]+"|" + board[4]+"|" + board[5]+"|")
        print("|" + board[6]+"|" + board[7]+"|" + board[8]+"|")

def play_game():
        display_board()

        while game_still_going:
                handle_turn(current_player)
                check_if_game_is_over()
                flip_player(current_player)

        if winner == "X":
                print("The winner is " + p1 + ", well played!")
        elif winner == "O":
                print("The winner is " + p2 + ", well played!")
        elif winner == None:
                print("The game is a tie.")
                

def handle_turn(player):
                print("Its "+ player + "'s turn.")
                position = int(input("Enter a position from 1-9 on the board: "))

                valid=False
                while valid == False:
                        if position >=1 and position <=9 and board[position-1] == '-':
                                valid=True
                        else:
                                print("This is not a valid position, enter another one.")
                                position = int(input("Enter a position from 1-9 on the board: "))
                position=int(position)-1
                board[position] = player
                
                display_board()

def flip_player(player):
        global current_player
        if player == "X":
                current_player ="O"
                word_current_player = p1
        elif player == "O":
                current_player="X"
                word_current_player = p2

def check_rows():
        global winner
        global game_still_going
        if board[0] =="X" and board[1]=="X" and board[2] =="X":
                winner = "X"
                game_still_going=False

        elif board[3] =="X" and board[4]=="X" and board[5] =="X":
                winner = "X"
                game_still_going=False

        elif board[6]==board[7]==board[8] =="X" != "-":
                winner = "X"
                game_still_going=False

        if board[0] =="O" and board[1]=="O" and board[2] =="O":
                winner = "O"
                game_still_going=False

        elif board[3] =="O" and board[4]=="O" and board[5] =="O":
                winner = "O"
                game_still_going=False

        elif board[6] =="O" and board[7]=="O" and board[8] =="O":
                winner = "O"
                game_still_going=False
        else:
                pass

def check_columns():
        global winner
        global game_still_going
        if board[0] =="X" and board[3]=="X" and board[6] =="X":
                winner = "X"
                game_still_going=False

        elif board[1] =="X" and board[4]=="X" and board[7] =="X":
                winner = "X"
                game_still_going=False

        elif board[2] =="X" and board[5]=="X" and board[8] =="X":
                winner = "X"
                game_still_going=False

        elif board[0] =="O" and board[3]=="O" and board[6] =="O":
                winner = "O"
                game_still_going=False

        elif board[1] =="O" and board[4]=="O" and board[7] =="O":
                winner = "O"
                game_still_going=False

        elif board[2] =="O" and board[5]=="O" and board[8] =="O":
                winner = "O"
                game_still_going=False
        else:
                pass

def check_diagonals():
        global winner
        global game_still_going
        if board[0] =="X" and board[4]=="X" and board[8] =="X":
                winner = "X"
                game_still_going=False

        elif board[2] =="X" and board[4]=="X" and board[6] =="X":
                winner = "X"
                game_still_going=False

        elif board[0] =="O" and board[4]=="O" and board[8] =="O":
                winner = "O"
                game_still_going=False

        elif board[2] =="O" and board[4]=="O" and board[6] =="O":
                winner = "O"
                game_still_going=False
        else:
                pass

def check_if_tie():
        if "-" not in board:
                game_still_going=False          

def check_if_winner():
        check_diagonals()
        check_columns()
        check_rows()

def check_if_game_is_over():
        check_if_winner()
        check_if_tie()
 
play_game()
