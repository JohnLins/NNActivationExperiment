import pygame, sys
from pygame.locals import *

import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pylab
import numpy as np
from activations import *
from neural import lossHistory
            

#from neural import *


#GRAPH ACTIVATION FUNCTION

actvFig = pylab.figure(figsize=[2, 2],dpi=100,)
lossFig = pylab.figure(figsize=[3.5, 3.5], dpi=100,)

actv = actvFig.gca()
lossg = lossFig.gca()



valueRange = []
index = -5.0
while index <= 5.0:
	valueRange.append(ReLU(index))
	index += .1




actv.plot(valueRange)
#lossg.plot(lossHistory)

actvCanvas = agg.FigureCanvasAgg(actvFig)
actvCanvas.draw()
actvRenderer = actvCanvas.get_renderer()
actvRawData = actvRenderer.tostring_rgb()


######################################


from neural import *

def matrixToInputVec(inputM):
    outputV = [[0 for row in range(0,4)] for col in range(0,4)]
    outputV[1] = inputM[0]
    outputV[2] = inputM[1]
    outputV[0] = inputM[2]
    outputV[3] = inputM[3]


    output2V = [[0 for row in range(0,4)] for col in range(0,4)]

    
    for i in range(4):
        output2V[i][1] = outputV[i][0]
        output2V[i][2] = outputV[i][1]
        output2V[i][0] = outputV[i][2]
        output2V[i][3] = outputV[i][3]

    return np.array(output2V).flatten()


def graph():
    # print(output)
    # print(outputValue)
    # print(lossHistory)

    pygame.init()
    pygame.display.set_caption("John's GUI NN")
    screenHeight = 700
    screenWidth = 1000
    DISPLAY=pygame.display.set_mode((screenWidth, screenHeight),0,32)
    screen = pygame.display.get_surface()

    WHITE=(255,255,255)
    BLACK = (0,0,0)
    BLUE=(0,0,255)

    DISPLAY.fill(WHITE)

    #GRAPH ACTIVATION
    screen.blit(pygame.image.fromstring(actvRawData, actvCanvas.get_width_height(), "RGB"), (0,0))
    
    

    

    #RENDER BLOCKS
    btnDim = 60
    positions = [[0 for row in range(0,4)] for col in range(0,4)]
    colors = [[BLACK for row in range(0,4)] for col in range(0,4)]
    #color = [[BLUE, BLUE, BLUE, BLUE],[]]
    color = BLACK
    #active = [[],[]]
    levels = [-35.0, 35.0, -105.0, 105.0]
    for i in range(4):
        for j in range(4):
            positions[i][j] = (screenWidth/2 - btnDim/2 + levels[j], screenHeight/2 - btnDim/2 + levels[i], btnDim, btnDim)

   


    print("positions", positions)
    print((positions[0][0][0]))
    print((positions[0][0][1]))

    #####################

    #RENDER BUTTON
    #pygame.draw.rect(DISPLAY, BLUE, (150,450,100,50))
    # myFont = pygame.font.SysFont("", 80)
    # myFont2 = pygame.font.SysFont("", 50)
    # GameName = myFont.render("Educational Maze Game", 1, (GREEN))
    # StartText = myFont2.render("START GAME", 1, (BLUE))
    # InstructionsText = myFont2.render("INSTRUCTIONS", 1, (BLUE))
    # window.blit(GameName, (100,50))
    # window.blit(StartText, (295,185))
    # window.blit(InstructionsText, (280,335))

    button = pygame.Rect((screenWidth/2) - 50, screenHeight - 120, 100, 50)

    # pos = pygame.mouse.get_pos()
    # (left,middle,right) = pygame.mouse.get_pressed()
    # if runBtn.collidepoint(pos):
    #     runBtn = pygame.draw.rect(DISPLAY, (50,200,160), Rect((215, 150), (400,100)))
    #     print("PRESSED")
    
    #############################
    clicked = [[0 for row in range(0,4)] for col in range(0,4)]


    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            
            
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = event.pos  # gets mouse position

                    # checks if mouse position is over the button

                    if button.collidepoint(mousePos):
                        # prints current location of mouse
                        print('button was pressed at {0}'.format(mousePos))
                        

                        # inputs = [1, 1, 1, 1, \
                        #           0, 1, 0, 1, \
                        #           1, 0, 0, 1, \
                        #           1, 1, 1, 1]    
                        # npInputs = np.array(inputs) 

                        #print("Output: ", predict(npInputs))
                        output = predict(matrixToInputVec(clicked))
                        print("Output2: ", output)

                        #lossg.clear()
                        
                        lossg.plot(lossHistory)

                        lossCanvas = agg.FigureCanvasAgg(lossFig)
                        lossCanvas.draw()
                        lossRenderer = lossCanvas.get_renderer()
                        lossRawData = lossRenderer.tostring_rgb()

                        

                        screen.blit(pygame.image.fromstring(lossRawData, lossCanvas.get_width_height(), "RGB"), (1,screenHeight/2 - 120))



                        # Display output
                        ouputText = pygame.font.SysFont(None, 28).render( (str(output[1])) + " : " + str(output[0]), True, (0, 0, 255), (255, 255, 255))
                        ouputTextRect = ouputText.get_rect()
                        ouputTextRect.centerx = screenWidth - 150
                        ouputTextRect.centery = screenHeight / 2
                        DISPLAY.blit(ouputText, ouputTextRect)

                    print("X: ", mousePos[0])
                    print("Y: ", mousePos[1])
                    # if mousePos[0] >= 100 and mousePos[0] <= 200 and mousePos[1] >= 100 and mousePos[1] <= 200:
                    #     color = BLUE
                    #     print("CLICKED")
                    # if mousePos[0] >= (positions[0][0][0] - 30) and mousePos[0] <= (positions[0][0][0] + 30) and mousePos[1] >= (positions[0][0][1] - 30) and mousePos[1] <= (positions[0][0][1] + 30):
                    #     color = BLUE
                    #     print("CLICKED")
                    for i in range(4):
                        for j in range(4):
                            if pygame.Rect(positions[i][j]).collidepoint(mousePos):
                                color = BLUE

                                if clicked[i][j] == 0:
                                    clicked[i][j] = 1
                                    colors[i][j] = BLUE
                                else:
                                    clicked[i][j] = 0
                                    colors[i][j] = BLACK
                                

                                print(matrixToInputVec(clicked))
                                print("WOW")




        for i in range(4):
            for j in range(4):
                pygame.draw.rect(DISPLAY, colors[i][j], positions[i][j])


        pygame.draw.rect(screen, [55, 55, 0], button)







        pygame.display.update()


