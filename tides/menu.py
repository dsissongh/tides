import pygame
import time
from pygame.locals import *
import pygame.font

def blitSurface():
	screen.blit(surface, (50,50) )
	pygame.display.update()


pygame.font.init()
screen = pygame.display.set_mode((640,480), 0, 32)
blitSurface()
time.sleep(4)