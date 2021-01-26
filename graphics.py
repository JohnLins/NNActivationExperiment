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
    levels = [-35.0, 35.0, -105.0, 105.0]
    for i in range(4):
        for j in range(4):
            positions[i][j] = (screenWidth/2 - btnDim/2 + levels[j], screenHeight/2 - btnDim/2 + levels[i], btnDim, btnDim)

   
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(DISPLAY,BLUE, positions[i][j])

            
    #####################3


    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


