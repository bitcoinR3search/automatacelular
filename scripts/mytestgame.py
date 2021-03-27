#usaremos la libreria pygame que tiene ya empaquetado
#funciones q reaccionan al movimiento, a los clicks, etc

import sys, pygame
import numpy as np
import matplotlib.pyplot as plt

pygame.init()

size=width,height=600,600

nX_cels = nY_cels = 60
dimCW= width/nX_cels
dimCH=height/nY_cels


bg=25,25,25


screen = pygame.display.set_mode(size)
screen.fill(bg)

gameState=np.random.randint(0,2,(nX_cels,nY_cels))
a = np.diag(range(15))
print(a)
print(gameState)


while 1:

	for y in range(1,nY_cels+1):
		for x in range(1,nX_cels+1):
			n_neigh = np.sum(gameState[x-1:x+2,y-1:y+2])-gameState[x,y]
			print(n_neigh)
			poly = [((x-1)*dimCW,(y-1)*dimCH),
						((x)*dimCW, (y-1)*dimCH),
						((x)*dimCW, (y)*dimCH),
						((x-1)*dimCW,(y)*dimCH)]

			plt.matshow(gameState)
			plt.show()

	#pygame.display.flip()   
#ta genial

