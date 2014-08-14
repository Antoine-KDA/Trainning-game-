#!/usr/bin/env python   
   #Import Modules

import os
import sys
import pygame
import time
import winsound
from pygame.locals import * 

if not pygame.font: print 'Warning, fonts disabled'


def main(cadena1,cadena2):
    cadena3="Pulse espacio para continuar"
   
#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((800,600),pygame.DOUBLEBUF)
    screen = pygame.display.set_mode((800,600),pygame.FULLSCREEN)
    if cadena1=="":
      cadena2="Fin del ejercicio"
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    
    background1 = pygame.Surface(screen.get_size())
    background1 = background1.convert()
    background1.fill((0, 0, 0))
    
    


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
        textpos3 = text3.get_rect(centerx=background1.get_width()/2,centery=450,)
        text4 = font.render("Fin del descanso", 1, (250, 250, 250))
        textpos4 = text4.get_rect(centerx=background1.get_width()/2, centery=150,)
        
        
#Display The Background      
     
    screen.blit(background, (0, 0))
    pygame.display.flip()
    if cadena1=="": 
      time.sleep(5)
      return
    else:
      time.sleep(100) #Esta espera hay que ponerla de 5 minutos
      winsound.PlaySound('ringout',winsound.SND_FILENAME)
      background1.blit(text3, textpos3)
      background1.blit(text4, textpos4)
      background1.blit(text2, textpos2)
      screen.blit(background1, (0, 0))
      pygame.display.flip()
      while 1:
        event = pygame.event.wait()
        #pygame.display.flip()
        if event.type is KEYDOWN and event.key == K_SPACE:
          #winsound.PlaySound('instruccion',winsound.SND_FILENAME)
          return
    
#main("Hola","Hola")


