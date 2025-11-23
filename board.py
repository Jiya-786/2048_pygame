import pygame

colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          'dark text': (119, 110, 101),
          "other" :(0,0,0),
          "bg" :(187,173,160)
          }

def board():
   pygame.draw.rect(screen,(196,164,132),[200,110,400,400],0,10)
   score_txt=font.render(f'Score:{score}',True,'black')
   high_score_txt=font.render(f'High Score:{high_score}',True,'black')
   screen.blit(high_score_txt,(10+200,410+110))
   screen.blit(score_txt,(10+200,450+110))

def no_moves_left(board):
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j+1]:
                return False

    for j in range(4):
        for i in range(3):
            if board[i][j] == board[i+1][j]:
                return False
    return True

def draw_over():
    pygame.draw.rect(screen,'black',[50+200,50+110,300,100],0,10)
    txt1=font.render("Game Over!",True,"white")
    txt2=font.render("Press Enter T0 Restart",True,'white')
    screen.blit(txt1,(130+200,65+110))
    screen.blit(txt2,(70+200,105+110))

def pieces(board):
    for i in range(4):
        for j in range(4):
            value=board[i][j]
            if value > 8:
                value_colour=colors["light text"]
            else:
                value_colour=colors["dark text"]
            if value<=2048:
                color=colors[value]
            else:
                color=colors["other"]
            pygame.draw.rect(screen,color,[j*95+20+200,i*95+20+110,75,75],0,5)
            if value>0:
                value_len=len(str(value))
                font =pygame.font.Font('freesansbold.ttf',48-(5*value_len))
                value_text=font.render(str(value),True,value_colour)
                text_rect=value_text.get_rect(center=(j*95+57+200,i*95+57+110))
                screen.blit(value_text,text_rect)
