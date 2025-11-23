#importing random
import random

#function for left,right,up,down commands
def take_turn(direc, board,score):
    #this variable is for ensuring that the game works properly
    merged = [[False for _ in range(4)] for _ in range(4)]
    if direc == 'UP':
        for i in range(4): #checcking every box
            for j in range(4):
                shift = 0
                # this condition is there because if i=0 then it cannot go up
                if i > 0:
                    #checking the upper blocks
                    for q in range(i):
                        #moving up by shift
                        if board[q][j] == 0:
                            shift += 1
                    if shift > 0:
                        #shiting the value
                        board[i - shift][j] = board[i][j]
                        #setting the block into zero
                        board[i][j] = 0 
                    # merging the blocks condition 
                    if board[i - shift - 1][j] == board[i - shift][j] and not merged[i - shift][j] \
                            and not merged[i - shift - 1][j]:
                        
                        board[i - shift - 1][j] *= 2
                        #incrementing the score
                        score += board[i - shift - 1][j]
                        board[i - shift][j] = 0
                        #merging conditon
                        merged[i - shift - 1][j] = True
# same logics as up
    elif direc == 'DOWN':
        for i in range(3):
            for j in range(4):
                shift = 0
                for q in range(i + 1):
                    if board[3 - q][j] == 0:
                        shift += 1
                if shift > 0:
                    board[2 - i + shift][j] = board[2 - i][j]
                    board[2 - i][j] = 0
                if 3 - i + shift <= 3:
                    if board[2 - i + shift][j] == board[3 - i + shift][j] and not merged[3 - i + shift][j] \
                            and not merged[2 - i + shift][j]:
                        board[3 - i + shift][j] *= 2
                        score += board[3 - i + shift][j]
                        board[2 - i + shift][j] = 0
                        merged[3 - i + shift][j] = True
# same logics as up
    elif direc == 'LEFT':
        for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board[i][q] == 0:
                        shift += 1
                if shift > 0:
                    board[i][j - shift] = board[i][j]
                    board[i][j] = 0
                if board[i][j - shift] == board[i][j - shift - 1] and not merged[i][j - shift - 1] \
                        and not merged[i][j - shift]:
                    board[i][j - shift - 1] *= 2
                    score += board[i][j - shift - 1]
                    board[i][j - shift] = 0
                    merged[i][j - shift - 1] = True
# same logics as up
    elif direc == 'RIGHT':
        for i in range(4):
            for j in range(4):
                shift = 0
                for q in range(j):
                    if board[i][3 - q] == 0:
                        shift += 1
                if shift > 0:
                    board[i][3 - j + shift] = board[i][3 - j]
                    board[i][3 - j] = 0
                if 4 - j + shift <= 3:
                    if board[i][4 - j + shift] == board[i][3 - j + shift] and not merged[i][4 - j + shift] \
                            and not merged[i][3 - j + shift]:
                        board[i][4 - j + shift] *= 2
                        score += board[i][4 - j + shift]
                        board[i][3 - j + shift] = 0
                        merged[i][4 - j + shift] = True
    return board,score
# creating  random pieces
def new_pieces(board): 
    count=0
    full =False
    # selcting zeroes and ensuring the loop runs only two times
    while any(0 in row for row in board) and count<1:
        # selcting random row,col
        row=random.randint(0,3)
        col=random.randint(0,3)
        
        if board[row][col]==0:
            count+=1
        # according to game the probability of spawning 2 should be more than 4
            if random.randint(1,10)==10:
                board[row][col] =4
            else:
                board[row][col]=2
    # checking one of the conditions for game over
    if count <1:
        full=True
    return board,full
