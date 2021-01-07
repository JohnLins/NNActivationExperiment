import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    pygame.display.set_caption("John's GUI NN")
    screenHeight = 700
    screenWidth = 1000
    DISPLAY=pygame.display.set_mode((screenWidth, screenHeight),0,32)

    WHITE=(255,255,255)
    BLUE=(0,0,255)

    DISPLAY.fill(WHITE)

    btnDim = 60
    positions = [[0 for row in range(0,4)] for col in range(0,4)]
    levels = [-35.0, 35.0, -105.0, 105.0]
    for i in range(4):
        for j in range(4):
            positions[i][j] = (screenWidth/2 - btnDim/2 + levels[j], screenHeight/2 - btnDim/2 + levels[i], btnDim, btnDim)

   
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(DISPLAY,BLUE, positions[i][j])



    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()
