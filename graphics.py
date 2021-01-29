import pygame, sys
from pygame.locals import *

import matplotlib
matplotlib.use("Agg")
import matplotlib.backends.backend_agg as agg
import pylab
from activations import *

#GRAPH ACTIVATION FUNCTION

fig = pylab.figure(figsize=[2, 2], # Inches
                   dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
ax = fig.gca()



valueRange = []
index = -5.0
while index <= 5.0:
	valueRange.append(ReLU(index))
	index += .1




ax.plot(valueRange)

canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()
######################################


from neural import *

def graph(output, outputValue, lossHistory):
    print(output)
    print(outputValue)
    print(lossHistory)

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
    size = canvas.get_width_height()
    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, (0,0))
    #pygame.display.flip()
    #######################

    """agg.title("Loss Graph")  
    agg.xlabel("Iterations")
    agg.ylabel("LOSS")  
    agg.plot(lossHistory, color ="red")  
    agg.show() """

    

    #RENDER BLOCKS
    btnDim = 60
    positions = [[0 for row in range(0,4)] for col in range(0,4)]
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
                        

                        inputs = [1, 1, 1, 1, \
                                  0, 1, 0, 1, \
                                  1, 0, 0, 1, \
                                  1, 1, 1, 1]    

                        print("Output: ", predict(np.array(inputs)))

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
                                clicked[i][j] = 1
                                print(clicked)
                                print("WOW")




        for i in range(4):
            for j in range(4):
                pygame.draw.rect(DISPLAY, color, positions[i][j])


        pygame.draw.rect(screen, [55, 55, 0], button)







        pygame.display.update()


