#!/usr/bin/env python   
   #Import Modules

import os
import sys
import pygame
import time
import winsound
from pygame.locals import * 

if not pygame.font: print 'Warning, fonts disabled'


def scores(p_d,p_i,p_b):

#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((800,600),pygame.DOUBLEBUF)
    screen = pygame.display.set_mode((800,600),pygame.FULLSCREEN)
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    
    cadena1="Ojo derecho: " +str(p_d)+" puntos"
    cadena2="Ojo izquierdo: " +str(p_i)+" puntos"
    cadena3="Binocular: " + str(p_b)+" puntos"
#Put Text On The Background, Centered
    if pygame.font:
        font = pygame.font.Font('freesansbold.ttf', 50)
        text1 = font.render(cadena1, 1, (250, 250, 250))
        textpos1 = text1.get_rect(centerx=background.get_width()/2, centery=150,)
        background.blit(text1, textpos1)
        text2 = font.render(cadena2, 1, (250, 250, 250))
        textpos2 = text2.get_rect(centerx=background.get_width()/2,centery=background.get_height()/2,)
        background.blit(text2, textpos2)
        text3 = font.render(cadena3, 1, (250, 250, 250))
        textpos3 = text3.get_rect(centerx=background.get_width()/2,centery=450,)
        background.blit(text3, textpos3)
       
        
        
#Display The Background      
     
    screen.blit(background, (0, 0))
    pygame.display.flip()
    time.sleep(20)

#scores(50,40,30)   

