#!/usr/bin/env python   
   #Import Modules

import os
import sys
import pygame
import time
import math
import winsound
import operator
from pygame.locals import * 
if not pygame.font: print 'Warning, fonts disabled'
def saludo():
    #global start
#Initialize Everything
    ojos=["derecho","izquierdo"]
    cadena3="Pulse espacio para continuar"
    i=0
    pygame.init() 
    screen = pygame.display.set_mode((800,600),pygame.FULLSCREEN )
    seg=time.time()
    
    dias=seg/86400
    entero=round(dias)
    var=entero % 2
    var=int(var)
    if var>0:
      i=1


#Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

#Put Text On The Background, Centered
    if pygame.font:
        ft = pygame.font.Font('freesansbold.ttf', 50)
        text = ft.render("Cubra el ojo "+ojos[i], 1, (250, 250, 250))
        textpos = text.get_rect(centerx=background.get_width()/2,centery=background.get_height()/2,)
        background.blit(text, textpos)
        text3 = ft.render(cadena3, 1, (250, 250, 250))
        textpos3 = text3.get_rect(centerx=background.get_width()/2,centery=450,)
        background.blit(text3, textpos3)


#Display The Background
    screen.blit(background, (0, 0))
    #while not start:
    while 1:
        event = pygame.event.wait()
        pygame.display.flip()
        if event.type is KEYDOWN and event.key == K_SPACE:
        #  winsound.PlaySound('instruccion',winsound.SND_FILENAME)
            return i
    
#winsound.PlaySound('instruccion',winsound.SND_FILENAME)
#if not pygame.font: print 'Warning, fonts disabled'
#saludo()

