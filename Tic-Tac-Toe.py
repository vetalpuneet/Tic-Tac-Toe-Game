def is_winner(board):
    winner = {0 : 'Nobody', 1 : 'Player 1', 2 : 'Player 2'}
    #print(board[0] == [1,1,1])
    for ele in range(1, 3):
        if board[0] == [ele, ele, ele] or board[1] == [ele, ele, ele] or board[2] == [ele, ele, ele]:
            print("Horizontal match")
            return winner[ele]
        elif board[0][0] == ele and board[1][0] == ele and board[2][0] == ele:
            print("Vertical match")
            return winner[ele]
        elif board[0][1] == ele and board[1][1] == ele and board[2][1] == ele:
            print("Vertical match")
            return winner[ele]
        elif board[0][2] == ele and board[1][2] == ele and board[2][2] == ele:
            print("Vertical match")
            return winner[ele]
        elif board[0][0] == ele and board[1][1] == ele and board[2][2] == ele:
            print("Diagonal match")
            return winner[ele]
        elif board[0][2] == ele and board[1][1] == ele and board[2][0] == ele:
            print("Diagonal match")
            return winner[ele]
    #print("Returning Nobody")
    return winner[0]
    
def move(k, board):
    r1 = int(input('what is the row ? '))
    c1 = int(input('what is the column ? '))
    if k % 2 == 0:
        if(board[r1][c1] == 0):
            board[r1][c1] = 1
        else:
            print('Invalid position')
    else:
        if(board[r1][c1] == 0):
            board[r1][c1] = 2
        else:
            print('Invalid position')
    print(board) 
    

def main():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    print(board)
    #winner_player = is_winner(board)
    #print('The TEST is: {}'.format(winner_player))
    #board_size = int(input('Enter board size: '))
    #print_board(board_size)
    k = 0
    while k < 10:
        move(k, board)
        winner_player = is_winner(board)
        #print(winner_player)
        if(winner_player == 'Nobody'):
            k = k+1
            #print('k incremented')
        elif(winner_player=='Player 1' or winner_player=='Player 2'):
            print('The winner player is: {}'.format(winner_player))
            break
    if k==10:
        print("The winner is Nobody")
main()    
