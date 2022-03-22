#TIC TAC TOE GAME completed on 22/3/2022
import pygame, sys
pygame.init()

#constant variables
SIZE = width, height = 600, 600
# BG_COLOR = '#14bdac' #cyan
BG_COLOR = (255, 255, 255) #cyan
GREEN = '#00D100'
LINE_COLOR = (66,66,66) #light grey
LINE_WIDTH = 10
CROSS_COLOR = (0, 0, 0) #grey
O_COLOR = (239, 231, 200) #white
BOARD_ROWS = 3
BOARD_COLS = 3
PADDING = width // 10
PADDING2 = 10
RADIUS = width // 10  #10 percent
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
CUT_LINE_WIDTH = 10
PLAYER1 = 1
PLAYER2 = 2
#one third of total width/height (since width == height in square) 
ONE_THIRD = width // 3
# current_player = PLAYER1


screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("TIC TAC TOE")





#logical board and initialising all to 0
board = []
for i in range(BOARD_ROWS):
    board.append([])
    for j in range(BOARD_COLS):
        board[i].append(0)


def place_marker(row, col, players_marker):   
    board[row][col] = players_marker  # 1 -> X   2 -> O


def slot_empty(row, col):
    return board[row][col] == 0

def board_full():
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i][j] == 0:
                return False
    return True

screen.fill(BG_COLOR) #overrides everything on screen


def draw_lines():
    #horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, height / 3), (width, height/3), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, (height / 3)*2), (width, (height / 3)*2), LINE_WIDTH)
    #vertical lines
    pygame.draw.line(screen, LINE_COLOR, (width/3, 0), (width/3, height), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, ((width/3)*2, 0), ((width/3)*2, height), LINE_WIDTH)


def draw_marker(row, col):
    if board[row][col] == PLAYER1:
        pygame.draw.line(screen, CROSS_COLOR, (col * ONE_THIRD + PADDING, row * ONE_THIRD + ONE_THIRD - PADDING), (col*ONE_THIRD + ONE_THIRD - PADDING, row * ONE_THIRD + PADDING), CROSS_WIDTH)
        pygame.draw.line(screen, CROSS_COLOR, (col * ONE_THIRD + PADDING, row * ONE_THIRD + PADDING ), (col*ONE_THIRD + ONE_THIRD - PADDING, row * ONE_THIRD + ONE_THIRD - PADDING), CROSS_WIDTH )
    else:
        pygame.draw.circle(screen, O_COLOR,( int(col * ONE_THIRD + height/6), int(row * ONE_THIRD + height/6) ), RADIUS, CIRCLE_WIDTH)

        



def switch_player(current_player):
    if current_player == PLAYER1:
        return PLAYER2
    else:
        return PLAYER1


def check_for_win():
    horizontal = -1
    vertical = -2
    diagonal = -3

    for i in range(3):
        #check horizontally
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0], i, horizontal
        #check vertically
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i], i, vertical
    
    #diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0], 0, diagonal
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2], 1, diagonal
    
    return 0,0,0

#crosses the matching rows, columns or diagonals if anyone wins
def cross_row_or_col(winner, row_or_col, direction):
    if winner == 1:
        cut_color = CROSS_COLOR
    else:
        cut_color = O_COLOR


    if direction == -1:
        pygame.draw.line(screen, cut_color, (0+PADDING2, row_or_col*ONE_THIRD+height/6), (width-PADDING2, row_or_col*ONE_THIRD+height/6), CUT_LINE_WIDTH)
    elif direction == -2:
        pygame.draw.line(screen, cut_color, (row_or_col*ONE_THIRD+height/6, 0+PADDING2), (row_or_col*ONE_THIRD+height/6,width-PADDING2), CUT_LINE_WIDTH)
    elif direction == -3:
        if row_or_col == 0: # 0 -> descending diagonal
            pygame.draw.line(screen, cut_color, (0+PADDING2,0+PADDING2), (width-PADDING2, width-PADDING2), CUT_LINE_WIDTH)
        else: # 1 -> ascending diagonal
            pygame.draw.line(screen, cut_color, (0+PADDING2, width-PADDING2), (width-PADDING2, 0+PADDING2), CUT_LINE_WIDTH)
  

def restart():
    global board
    screen.fill(BG_COLOR)
    draw_lines()
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            board[i][j] = 0
    main()

# main loop
def main():
    current_player = PLAYER1
    draw_lines()
    game_over = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                #collecting mouse x and y coordinates where clicked
                mX = event.pos[0] #0 -> x
                mY = event.pos[1] #1 -> y

                row_clicked = int(mY // (height / 3))
                col_clicked = int(mX // (width / 3))

                if slot_empty(row_clicked, col_clicked):
                    place_marker(row_clicked, col_clicked, current_player)
                    draw_marker(row_clicked, col_clicked)
                    winner, row_or_col_to_cross, direction = check_for_win()
                    current_player = switch_player(current_player) 
                if winner == 1 or winner ==2:
                    print("winner is " + str(winner))
                    cross_row_or_col(winner, row_or_col_to_cross, direction)
                    game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                    
        
        pygame.display.update()



if __name__ == "__main__":
    main()