#!/usr/bin/env python
"""Entrenamiento visual"""


############################
#  Importancion de modulos #
############################

import VisionEgg
VisionEgg.start_default_logging(); VisionEgg.watch_exceptions()

from VisionEgg.Core import *
from VisionEgg.FlowControl import Presentation, FunctionController
from VisionEgg.MoreStimuli import *
import random
import pygame
import os
import espera
import inicio
import puntos
import math
import sys
import pygame
import time
import winsound
from pygame.locals import * 
if not pygame.font: print 'Warning, fonts disabled'


########################################
#  Inicializacion de variables OpenGL  #
########################################

ojo=inicio.saludo()
#ojo=1

screen = get_default_screen()

screen.parameters.bgcolor = (0.0,0.0,0.0,0.0)

fixcirc = FilledCircle(
  anchor   = 'center',
  position = (screen.size[0]/2.0, screen.size[1]/2.0),
  radius   = 4.0,
  color    = (0.7, 0, 0)
)

#definicion del punto de fijacion
fixpoint = Arrow(
  anchor      = 'center',
  position    = (screen.size[0]/2.0, screen.size[1]/2.0),
  size        = (50, 8),
  #color       = (1.0, 1.0, 1.0),
  color    = (0.5, 0.5, 0.5)

)

#estimulo cuadrado de 8 pixeles

target = Target2D(
  anchor = 'left',
  size   = (8.0,8.0)
)

  
#inicializacion de variables

divx = 9
divy = 9
wx = screen.size[0]/divx
wy = screen.size[1]/divy
coord = []
right = 0
left = 0
up = 0
down = 0
rad1 = 0.0
rad2 = 0.0
inten = 0.0
logfile = 0
ojos=["I","D","B"]
ojos_=["Derecho","Izquierdo"]
filename = time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '_vf_'+ojos[ojo] + '.log'
xpos = 0
ypos = 0
end = 0
start = 0
i = 0
anrad=0
angrad=0
p_i=0
p_d=0
p_b=0
falsos=0


#rutinas para los eventos del teclado

def keydown(event):
    global up, down, right, left
    if event.key == pygame.locals.K_RIGHT:
        right = 1
    elif event.key == pygame.locals.K_LEFT:
        left = 1
    elif event.key == pygame.locals.K_UP:
        up = 1
    elif event.key == pygame.locals.K_DOWN:
        down = 1
    elif event.key == pygame.locals.K_SPACE:
        register(event)
    if event.key == pygame.locals.K_ESCAPE:
        quit_app(event)
    if event.key == pygame.locals.K_SPACE:
        init(event)

def keyup(event):
    global up, down, right, left
    if event.key == pygame.locals.K_RIGHT:
        right = 0
    elif event.key == pygame.locals.K_LEFT:
        left = 0
    elif event.key == pygame.locals.K_UP:
        up = 0
    elif event.key == pygame.locals.K_DOWN:
        down = 0

def settings(t=None):
    global stimulus, right, left, rad, up, down
    if right:
        rad1 = fixpoint.parameters.size[0] + 1
        rad2 = fixpoint.parameters.size[1] + 0.25
        fixpoint.parameters.size = (rad1, rad2)
    elif left:
        rad1 = fixpoint.parameters.size[0] - 1
        rad1 = max(rad1, 24)
        rad2 = fixpoint.parameters.size[1] - 0.25
        rad2 = max(rad2, 6)
        fixpoint.parameters.size = (rad1, rad2)
    elif up:
        rad = (fixpoint.parameters.orientation - 1) % 360
        fixpoint.parameters.orientation = rad
    elif down:
        rad = (fixpoint.parameters.orientation + 1) % 360
        fixpoint.parameters.orientation = rad
    
def quit_app(event):
    global end
    end = 1
    p.parameters.go_duration = (0,'frames')
    #return

def init(event):
    global start
    start = 1

#rutina para el registro de los datos
    
def register(event):
    global coord,xpos,ypos,inten,matriz,mat3,mat6,mat1,falsos
    #print ("En register")
    (xpos,ypos)=target.parameters.position
    i=int(xpos/wx)
    j=int((ypos-2.5)/wy)
    if inten >0:
      #matriz[i][j]=inten
      if inten==0.33:
        mat3[i][j]=1
        matriz[i][j]=3
      elif inten==0.66:
        mat6[i][j]=1
        if matriz[i][j]<2:
           matriz[i][j]=2
      else:
        mat1[i][j]=1
        if matriz[i][j]<1:
           matriz[i][j]=1
    else: 
      falsos=falsos+1
    
#Tres metodos para la gestion de la puntuacion
def zeros(*shape):
  if len(shape) == 0:
    return 0
  car = shape[0]
  cdr = shape[1:]
  return [zeros(*cdr) for i in range(car)]  

  
def guarda_scores(nota,filename):
    logfile=open(filename,'a')
    logfile.write(time.strftime("%Y%m%d_%H%M%S", time.localtime())+' '+str(nota)+'\n')
    logfile.close()
    
def guarda_resul():
   global filename, logfile,wx,wy,matriz,divx,divy
   logfile=open(filename,'a')
   logfile.write(str(divx)+'\n')
   logfile.write(str(divy)+'\n')
   logfile.write(str(falsos)+'\n')
   for i in range(1,divx):
      for j in range(1,divy):
        #if matriz[i][j]>0:
          #logfile=open(filename,'a')
          xposi=wx*i
          yposi=wy*j+2.5
          intens3=mat3[i][j]
          intens6=mat6[i][j]
          intens1=mat1[i][j]
          logfile.write(str(xposi)+' '+str(yposi)+' '+str(intens3)+' '+str(intens6)+' '+str(intens1)+'\n')
          #logfile.close()
    
   logfile.close()
    
  
def recuento():
  global matriz,p_i,p_b,p_d
  suma=0
  for i in range(1,divx):
      for j in range(1,divy):
        if matriz[i][j]==3:
          suma+=3
        elif matriz[i][j]==2:
          suma+=2
        elif matriz[i][j]==1:
          suma+=1
          
  if ojo==0:
      p_i=suma
      guarda_scores(p_i,"Ptos_I.log")
  elif ojo==1:
      p_d=suma
      guarda_scores(p_d,"Ptos_D.log")
  else:
      p_b=suma
      guarda_scores(p_b,"Ptos_B.log")
  #print suma
 

#Métodos para generar estimulos de forma aleatoria
def pintaMatriz():
  global matriz
  for i in range(1,divx):
      for j in range(1,divy):
       print matriz[i][j]
#generamos una lista aleatoria para la posicion de los estimulos
        
def shuffle(lst):
    "randomize a list"
    for i in range(len(lst)-1,0,-1):
        choice = int(random.random()*i)
        lst[choice], lst[i] = lst[i], lst[choice]
def rellenar():
  global coord
  #pos=[0.4,0.5,0.6,0.7,0.8]
  for i in range(1,divx):
      for j in range(1,divy):
        coord.append((wx*i,wy*j+2.5,0.33))
        coord.append((wx*i,wy*j+2.5,0.66))
        coord.append((wx*i,wy*j+2.5,1.0)) 
        if(i%3==0):
          coord.append((wx*i,wy*j+2.5,0))    
        
def aplicacion():
  global p,inten,coord
  pos=[0.4,0.5,0.6,0.7,0.8]
  pos2=[1.3,1.4,1.5,1.6,1.7,1.8]
  rellenar()
  shuffle(coord)
  i = len(coord)-1
  target.parameters.position = coord[i][:2]
  (xpos,ypos)=target.parameters.position
  x=xpos-screen.size[0]/2
  y=ypos-screen.size[1]/2
  anrad=math.atan2(y, x)
  angrad=math.degrees(anrad)
 
  if angrad>=0:
      if angrad<=90: 
        orientacion=-45
        xx=2.0
        yy=2.0
      else:
       orientacion=-135
       xx=-2.0
       yy=2.0
  else:
      aux=angrad*(-1)
      if aux<=90:
        orientacion=45
        xx=2.0
        yy=-2.0
      else:
        orientacion=135
        xx=-2.0
        yy=-2.0
  
  fixpoint.parameters.position=((screen.size[0]/2.0)+xx, (screen.size[1]/2.0)+yy)
  fixpoint.parameters.orientation=orientacion
  
  
  viewport = Viewport(screen=screen, stimuli=[fixpoint,fixcirc])
  p = Presentation(go_duration=(1.0,'seconds'),viewports=[viewport])
  p.parameters.handle_event_callbacks = [(pygame.locals.KEYDOWN, keydown),
                                       (pygame.locals.KEYUP, keyup),
                                       (pygame.locals.QUIT, quit_app)]
  p.add_controller(None, None, FunctionController(during_go_func=settings))
  #winsound.PlaySound('instruccion',winsound.SND_FILENAME)
  p.go()
  
  while len(coord)!= 0:
    if end:
        break
    i = len(coord)-1
    target.parameters.position = coord[i][:2]
    dur=pos[random.randrange(0,4,1)]
    (xpos,ypos)=target.parameters.position
    x=xpos-screen.size[0]/2
    y=ypos-screen.size[1]/2
    anrad=math.atan2(y, x)
    angrad=math.degrees(anrad)
    #fixpoint.parameters.orientation=(-angrad) 
    if angrad>=0:
      if angrad<=90: 
        orientacion=-45
        xx=2.0
        yy=2.0
      else:
       orientacion=-135
       xx=-2.0
       yy=2.0
    else:
      aux=angrad*(-1)
      if aux<=90:
        orientacion=45
        xx=2.0
        yy=-2.0
      else:
        orientacion=135
        xx=-2.0
        yy=-2.0
  
    fixpoint.parameters.position=((screen.size[0]/2.0)+xx, (screen.size[1]/2.0)+yy)
    fixpoint.parameters.orientation=orientacion
    
  
    viewport = Viewport(screen=screen, stimuli=[fixpoint,fixcirc])
    p = Presentation(go_duration=(dur,'seconds'),viewports=[viewport])
    p.parameters.handle_event_callbacks = [ (pygame.locals.QUIT, quit_app)]
	
    
    p.add_controller(None, None, FunctionController(during_go_func=settings))
    p.go()

    inten = coord[i][-1]
    target.parameters.color = (1.0,1.0,1.0,inten)      #Se muestra el estimulo Duracion 0.3 segundos
    viewport = Viewport(screen=screen, stimuli=[target,fixpoint,fixcirc])
    p = Presentation(go_duration=(0.3,'seconds'),viewports=[viewport])
    p.parameters.handle_event_callbacks = [ (pygame.locals.QUIT, quit_app)]
                          
    p.add_controller(None, None, FunctionController(during_go_func=settings))
    p.go()
    target.parameters.color = (0.0,0.0,0.0,1.0)  #Desaparece el estimulo tiempo para registrar
    viewport = Viewport(screen=screen, stimuli=[target,fixpoint,fixcirc])
    dur2=pos[random.randrange(0,4,1)]
    p = Presentation(go_duration=(dur2,'seconds'),viewports=[viewport])
    p.parameters.handle_event_callbacks = [(pygame.locals.KEYDOWN, keydown),
                                       (pygame.locals.KEYUP, keyup),
                                       (pygame.locals.QUIT, quit_app)]
    p.add_controller(None, None, FunctionController(during_go_func=settings))
    p.go()
    coord.pop()

    
matriz=zeros(divx,divy)
mat1=zeros(divx,divy)
mat3=zeros(divx,divy)
mat6=zeros(divx,divy)
aplicacion()
recuento()
guarda_resul()
#pintaMatriz()
if ojo==0:
  ojo=1
else:
  ojo=0
espera.main("Descanso de 2 minutos","Cubra el ojo "+ojos_[ojo])
screen = get_default_screen()
screen.parameters.bgcolor = (0.0,0.0,0.0,0.0)
start=0
end=0
filename = time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '_vf_'+ojos[ojo] + '.log'
matriz=zeros(divx,divy)
mat1=zeros(divx,divy)
mat3=zeros(divx,divy)
mat6=zeros(divx,divy)
falsos=0
aplicacion()
recuento()
guarda_resul()
espera.main("Descanso de 2 minutos","Destape los dos ojos")
screen = get_default_screen()
screen.parameters.bgcolor = (0.0,0.0,0.0,0.0)
start=0
end=0
ojo=2
filename = time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '_vf_'+ojos[ojo] + '.log'
matriz=zeros(divx,divy)
mat1=zeros(divx,divy)
mat3=zeros(divx,divy)
mat6=zeros(divx,divy)
falsos=0
aplicacion()
recuento()
guarda_resul()
puntos.scores(p_d,p_i,p_b)





